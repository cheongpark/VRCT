from deepl import Translator as deepl_Translator
from deepl_translate import translate as deepl_web_Translator
from translators import translate_text as other_web_Translator
from languages import translators, translation_lang

# Translator
class Translator():
    def __init__(self):
        self.translator_status = {}
        for translator in translators:
            self.translator_status[translator] = False
        self.deepl_client = None

    def authentication(self, translator_name, authkey=None):
        result = False
        try:
            if translator_name == "DeepL(web)":
                self.translator_status["DeepL(web)"] = True
                result = True
            elif translator_name == "DeepL(auth)":
                self.deepl_client = deepl_Translator(authkey)
                self.deepl_client.translate_text(" ", target_lang="EN-US")
                self.translator_status["DeepL(auth)"] = True
                result = True
            elif translator_name == "Google(web)":
                self.translator_status["Google(web)"] = True
                result = True
            elif translator_name == "Bing(web)":
                self.translator_status["Bing(web)"] = True
                result = True
        except:
            pass
        return result

    def translate(self, translator_name, source_language, target_language, message):
        result = ""
        try:
            source_language=translation_lang[translator_name][source_language]
            target_language=translation_lang[translator_name][target_language]
            if translator_name == "DeepL(web)":
                result = deepl_web_Translator(
                    source_language=source_language,
                    target_language=target_language,
                    text=message
                    )
            elif translator_name == "DeepL(auth)":
                result = self.deepl_client.translate_text(
                    message,
                    source_lang=source_language,
                    target_lang=target_language,
                    ).text
            elif translator_name == "Google(web)":
                result = other_web_Translator(
                    query_text=message,
                    translator="google",
                    from_language=source_language,
                    to_language=target_language,
                    )
            elif translator_name == "Bing(web)":
                result = other_web_Translator(
                    query_text=message,
                    translator="bing",
                    from_language=source_language,
                    to_language=target_language,
                    )
        except:
            pass
        return result