from time import sleep
from queue import Queue
from threading import Thread
from requests import get as requests_get

from translation import Translator
from flashtext import KeywordProcessor
from osc_tools import send_typing, send_message, send_test_action, receive_osc_parameters
from languages import transcription_lang
from audio_utils import get_input_device_list, get_output_device_list, get_default_output_device
from audio_recorder import SelectedMicRecorder, SelectedSpeakerRecorder
from audio_recorder import SelectedMicEnergyRecorder, SelectedSpeakeEnergyRecorder
from audio_transcriber import AudioTranscriber
from utils import print_textbox, thread_fnc
from config import config
from notification import notification_xsoverlay_for_vrct

class Model:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Model, cls).__new__(cls)
            cls._instance.init()
        return cls._instance

    def init(self):
        self.mic_energy_recorder = None
        self.mic_energy_plot_progressbar = None
        self.speaker_energy_get_progressbar = None
        self.speaker_energy_plot_progressbar = None
        self.translator = Translator()
        self.keyword_processor = KeywordProcessor()

    def resetTranslator(self):
        del self.translator
        self.translator = Translator()

    def resetKeywordProcessor(self):
        del self.translator
        self.keyword_processor = KeywordProcessor()

    def authenticationTranslator(self, choice_translator=None, auth_key=None):
        if choice_translator == None:
            choice_translator = config.CHOICE_TRANSLATOR
        if auth_key == None:
            auth_key = config.AUTH_KEYS[choice_translator]

        result = self.translator.authentication(choice_translator, auth_key)
        if result:
            auth_keys = config.AUTH_KEYS
            auth_keys[choice_translator] = auth_key
            config.AUTH_KEYS = auth_keys
        return result

    def getTranslatorStatus(self):
        return self.translator.translator_status[config.CHOICE_TRANSLATOR]

    def getListTranslatorName(self):
        return list(self.translator.translator_status.keys())

    def getInputTranslate(self, message):
        translation = self.translator.translate(
                        translator_name=config.CHOICE_TRANSLATOR,
                        source_language=config.INPUT_SOURCE_LANG,
                        target_language=config.INPUT_TARGET_LANG,
                        message=message
                )
        message = config.MESSAGE_FORMAT.replace("[message]", message).replace("[translation]", translation)
        return message

    def getOutputTranslate(self, message):
        translation = self.translator.translate(
                        translator_name=config.CHOICE_TRANSLATOR,
                        source_language=config.OUTPUT_SOURCE_LANG,
                        target_language=config.OUTPUT_TARGET_LANG,
                        message=message
                )
        message = config.MESSAGE_FORMAT.replace("[message]", message).replace("[translation]", translation)
        return message

    def addKeywords(self):
        for f in config.INPUT_MIC_WORD_FILTER:
            self.keyword_processor.add_keyword(f)

    def checkKeywords(self, message):
        return len(self.keyword_processor.extract_keywords(message)) != 0

    @staticmethod
    def oscStartSendTyping():
        send_typing(True, config.OSC_IP_ADDRESS, config.OSC_PORT)

    @staticmethod
    def oscStopSendTyping():
        send_typing(False, config.OSC_IP_ADDRESS, config.OSC_PORT)

    @staticmethod
    def oscSendMessage(message):
        send_message(message, config.OSC_IP_ADDRESS, config.OSC_PORT)

    @staticmethod
    def oscCheck():
        def check_osc_receive(address, osc_arguments):
            if config.ENABLE_OSC is False:
                config.ENABLE_OSC = True

        # start receive osc
        th_receive_osc_parameters = Thread(target=receive_osc_parameters, args=(check_osc_receive,))
        th_receive_osc_parameters.daemon = True
        th_receive_osc_parameters.start()

        # check osc started
        send_test_action()

        # check update
        response = requests_get(config.GITHUB_URL)
        tag_name = response.json()["tag_name"]
        if tag_name != config.VERSION:
            config.UPDATE_FLAG = True

    @staticmethod
    def getListInputHost():
        return [host for host in get_input_device_list().keys()]

    @staticmethod
    def getListInputDevice():
        return [device["name"] for device in get_input_device_list()[config.CHOICE_MIC_HOST]]

    @staticmethod
    def getInputDefaultDevice():
        return [device["name"] for device in get_input_device_list()[config.CHOICE_MIC_HOST]][0]

    @staticmethod
    def getListOutputDevice():
        return [device["name"] for device in get_output_device_list()]

    @staticmethod
    def checkSpeakerStatus(choice=config.CHOICE_SPEAKER_DEVICE):
        speaker_device = [device for device in get_output_device_list() if device["name"] == choice][0]
        if get_default_output_device()["index"] == speaker_device["index"]:
            return True
        return False

    def startMicTranscript(self, log, send_log, system_log):
        mic_audio_queue = Queue()
        self.mic_audio_recorder = SelectedMicRecorder(
            [device for device in get_input_device_list()[config.CHOICE_MIC_HOST] if device["name"] == config.CHOICE_MIC_DEVICE][0],
            config.INPUT_MIC_ENERGY_THRESHOLD,
            config.INPUT_MIC_DYNAMIC_ENERGY_THRESHOLD,
            config.INPUT_MIC_RECORD_TIMEOUT,
        )
        self.mic_audio_recorder.record_into_queue(mic_audio_queue)
        mic_transcriber = AudioTranscriber(
            speaker=False,
            source=self.mic_audio_recorder.source,
            phrase_timeout=config.INPUT_MIC_PHRASE_TIMEOUT,
            max_phrases=config.INPUT_MIC_MAX_PHRASES,
        )
        def mic_transcript_to_chatbox():
            mic_transcriber.transcribe_audio_queue(mic_audio_queue, transcription_lang[config.INPUT_MIC_VOICE_LANGUAGE])
            message = mic_transcriber.get_transcript()
            if len(message) > 0:
                # word filter
                if self.checkKeywords(message):
                    print_textbox(log, f"Detect WordFilter :{message}", "INFO")
                    print_textbox(system_log, f"Detect WordFilter :{message}", "INFO")
                    return

                # translate
                if config.ENABLE_TRANSLATION is False:
                    voice_message = f"{message}"
                elif self.getTranslatorStatus() is False:
                    print_textbox(log,  "Auth Key or language setting is incorrect", "ERROR")
                    print_textbox(system_log, "Auth Key or language setting is incorrect", "ERROR")
                    voice_message = f"{message}"
                else:
                    voice_message = self.getInputTranslate(message)

                if config.ENABLE_TRANSCRIPTION_SEND is True:
                    if config.ENABLE_OSC is True:
                        # osc send message
                        model.oscSendMessage(voice_message)
                    else:
                        print_textbox(log, "OSC is not enabled, please enable OSC and rejoin.", "ERROR")
                        print_textbox(system_log, "OSC is not enabled, please enable OSC and rejoin.", "ERROR")
                    # update textbox message log
                    print_textbox(log,  f"{voice_message}", "SEND")
                    print_textbox(send_log, f"{voice_message}", "SEND")

        self.mic_print_transcript = thread_fnc(mic_transcript_to_chatbox)
        self.mic_print_transcript.daemon = True
        self.mic_print_transcript.start()

    def stopMicTranscript(self):
        if isinstance(self.mic_print_transcript, thread_fnc):
            self.mic_print_transcript.stop()
        if self.mic_audio_recorder.stop != None:
            self.mic_audio_recorder.stop()
            self.mic_audio_recorder.stop = None

    def startCheckMicEnergy(self, progressBar):
        def progressBarInputMicEnergyPlot():
            if mic_energy_queue.empty() is False:
                energy = mic_energy_queue.get()
                try:
                    progressBar.set(energy/config.MAX_MIC_ENERGY_THRESHOLD)
                except:
                    pass
            sleep(0.01)
        mic_energy_queue = Queue()
        mic_device = [device for device in get_input_device_list()[config.CHOICE_MIC_HOST] if device["name"] == config.CHOICE_MIC_DEVICE][0]
        self.mic_energy_recorder = SelectedMicEnergyRecorder(mic_device)
        self.mic_energy_recorder.record_into_queue(mic_energy_queue)
        self.mic_energy_plot_progressbar = thread_fnc(progressBarInputMicEnergyPlot)
        self.mic_energy_plot_progressbar.daemon = True
        self.mic_energy_plot_progressbar.start()

    def stopCheckMicEnergy(self):
        if self.mic_energy_recorder != None:
            self.mic_energy_recorder.stop()
        if self.mic_energy_plot_progressbar != None:
            self.mic_energy_plot_progressbar.stop()

    def startSpeakerTranscript(self, log, receive_log, system_log):
        spk_audio_queue = Queue()
        spk_device = [device for device in get_output_device_list() if device["name"] == config.CHOICE_SPEAKER_DEVICE][0]
        self.spk_audio_recorder = SelectedSpeakerRecorder(
            spk_device,
            config.INPUT_SPEAKER_ENERGY_THRESHOLD,
            config.INPUT_SPEAKER_DYNAMIC_ENERGY_THRESHOLD,
            config.INPUT_SPEAKER_RECORD_TIMEOUT,
        )
        self.spk_audio_recorder.record_into_queue(spk_audio_queue)
        spk_transcriber = AudioTranscriber(
            speaker=True,
            source=self.spk_audio_recorder.source,
            phrase_timeout=config.INPUT_SPEAKER_PHRASE_TIMEOUT,
            max_phrases=config.INPUT_SPEAKER_MAX_PHRASES,
        )
        def spk_transcript_to_textbox():
            spk_transcriber.transcribe_audio_queue(spk_audio_queue, transcription_lang[config.INPUT_SPEAKER_VOICE_LANGUAGE])
            message = spk_transcriber.get_transcript()
            if len(message) > 0:
                # translate
                if config.ENABLE_TRANSLATION is False:
                    voice_message = f"{message}"
                elif model.getTranslatorStatus() is False:
                    print_textbox(log, "Auth Key or language setting is incorrect", "ERROR")
                    print_textbox(system_log, "Auth Key or language setting is incorrect", "ERROR")
                    voice_message = f"{message}"
                else:
                    voice_message = model.getOutputTranslate(message)

                if config.ENABLE_TRANSCRIPTION_RECEIVE is True:
                    # update textbox message receive log
                    print_textbox(log,  f"{voice_message}", "RECEIVE")
                    print_textbox(receive_log, f"{voice_message}", "RECEIVE")
                    if config.ENABLE_NOTICE_XSOVERLAY is True:
                        notification_xsoverlay_for_vrct(content=f"{voice_message}")

        self.spk_print_transcript = thread_fnc(spk_transcript_to_textbox)
        self.spk_print_transcript.daemon = True
        self.spk_print_transcript.start()

    def stopSpeakerTranscript(self):
        if isinstance(self.spk_print_transcript, thread_fnc):
            self.spk_print_transcript.stop()
        if self.spk_audio_recorder.stop != None:
            self.spk_audio_recorder.stop()
            self.spk_audio_recorder.stop = None

    def startCheckSpeakerEnergy(self, progressBar):
        def progressBar_input_speaker_energy_plot():
            if speaker_energy_queue.empty() is False:
                energy = speaker_energy_queue.get()
                try:
                    progressBar.set(energy/config.MAX_SPEAKER_ENERGY_THRESHOLD)
                except:
                    pass
            sleep(0.01)

        def progressBar_input_speaker_energy_get():
            with self.speaker_energy_recorder.source as source:
                energy = self.speaker_energy_recorder.recorder.listen_energy(source)
                self.speaker_energy_queue.put(energy)

        speaker_device = [device for device in get_output_device_list() if device["name"] == config.CHOICE_SPEAKER_DEVICE][0]
        speaker_energy_queue = Queue()
        self.speaker_energy_recorder = SelectedSpeakeEnergyRecorder(speaker_device)
        self.speaker_energy_get_progressbar = thread_fnc(progressBar_input_speaker_energy_get)
        self.speaker_energy_get_progressbar.daemon = True
        self.speaker_energy_get_progressbar.start()
        self.speaker_energy_plot_progressbar = thread_fnc(progressBar_input_speaker_energy_plot)
        self.speaker_energy_plot_progressbar.daemon = True
        self.speaker_energy_plot_progressbar.start()

    def stopCheckSpeakerEnergy(self):
        if self.speaker_energy_get_progressbar != None:
            self.speaker_energy_get_progressbar.stop()
        if self.speaker_energy_plot_progressbar != None:
            self.speaker_energy_plot_progressbar.stop()

model = Model()
