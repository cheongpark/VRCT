translatorEngine = ["DeepL", "DeepL_API", "Google", "Bing"]
translation_lang = {}
dict_deepl_languages = {
    "Japanese":"JA",
    "English":"EN",
    "Korean":"KO",
    "Bulgarian":"BG",
    "Chinese":"ZH",
    "Czech":"CS",
    "Danish":"DA",
    "Dutch":"NL",
    "Estonian":"ET",
    "Finnish":"FI",
    "French":"FR",
    "German":"DE",
    "Greek":"EL",
    "Hungarian":"HU",
    "Italian":"IT",
    "Latvian":"LV",
    "Lithuanian":"LT",
    "Polish":"PL",
    "Portuguese":"PT",
    "Romanian":"RO",
    "Russian":"RU",
    "Slovak":"SK",
    "Slovenian":"SL",
    "Spanish":"ES",
    "Swedish":"SV",
    "Indonesian":"ID",
    "Ukrainian":"UK",
    "Turkish":"TR",
    "Norwegian":"NB",
}
translation_lang["DeepL"] = {
    "source":dict_deepl_languages,
    "target":dict_deepl_languages,
}

dict_deepl_api_source_languages = {
    "Japanese":"ja",
    "English":"en",
    "Bulgarian":"bg",
    "Czech":"cs",
    "Danish":"da",
    "German":"de",
    "Greek":"el",
    "Spanish":"es",
    "Estonian":"et",
    "Finnish":"fi",
    "French":"fr",
    "Hungarian":"hu",
    "Indonesian":"id",
    "Italian":"it",
    "Korean":"ko",
    "Lithuanian":"lt",
    "Latvian":"lv",
    "Norwegian":"nb",
    "Dutch":"nl",
    "Polish":"pl",
    "Portuguese":"pt",
    "Romanian":"ro",
    "Russian":"ru",
    "Slovak":"sk",
    "Slovenian":"sl",
    "Swedish":"sv",
    "Turkish":"tr",
    "Ukrainian":"uk",
    "Chinese":"zh"
}
dict_deepl_api_target_languages = {
    "Japanese":"ja",
    "English American":"en-US",
    "English British":"en-GB",
    "Bulgarian":"bg",
    "Czech":"cs",
    "Danish":"da",
    "German":"de",
    "Greek":"el",
    "English":"en",
    "Spanish":"es",
    "Estonian":"et",
    "Finnish":"fi",
    "French":"fr",
    "Hungarian":"hu",
    "Indonesian":"id",
    "Italian":"it",
    "Korean":"ko",
    "Lithuanian":"lt",
    "Latvian":"lv",
    "Norwegian":"nb",
    "Dutch":"nl",
    "Polish":"pl",
    "Portuguese Brazilian":"pt-BR",
    "Portuguese European":"pt-PT",
    "Romanian":"ro",
    "Russian":"ru",
    "Slovak":"sk",
    "Slovenian":"sl",
    "Swedish":"sv",
    "Turkish":"tr",
    "Ukrainian":"uk",
    "Chinese":"zh"
}
translation_lang["DeepL_API"] = {
    "source": dict_deepl_api_source_languages,
    "target": dict_deepl_api_target_languages,
}

dict_google_languages = {
    "Japanese":"ja",
    "English":"en",
    "Chinese":"zh",
    "Arabic":"ar",
    "Russian":"ru",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Portuguese":"pt",
    "Italian":"it",
    "Korean":"ko",
    "Greek":"el",
    "Dutch":"nl",
    "Hindi":"hi",
    "Turkish":"tr",
    "Malay":"ms",
    "Thai":"th",
    "Vietnamese":"vi",
    "Indonesian":"id",
    "Hebrew":"he",
    "Polish":"pl",
    "Mongolian":"mn",
    "Czech":"cs",
    "Hungarian":"hu",
    "Estonian":"et",
    "Bulgarian":"bg",
    "Danish":"da",
    "Finnish":"fi",
    "Romanian":"ro",
    "Swedish":"sv",
    "Slovenian":"sl",
    "Persian/Farsi":"fa",
    "Bosnian":"bs",
    "Serbian":"sr",
    "Filipino":"tl",
    "Haitiancreole":"ht",
    "Catalan":"ca",
    "Croatian":"hr",
    "Latvian":"lv",
    "Lithuanian":"lt",
    "Urdu":"ur",
    "Ukrainian":"uk",
    "Welsh":"cy",
    "Swahili":"sw",
    "Samoan":"sm",
    "Slovak":"sk",
    "Afrikaans":"af",
    "Norwegian":"no",
    "Bengali":"bn",
    "Malagasy":"mg",
    "Maltese":"mt",
    "Gujarati":"gu",
    "Tamil":"ta",
    "Telugu":"te",
    "Punjabi":"pa",
    "Amharic":"am",
    "Azerbaijani":"az",
    "Belarusian":"be",
    "Cebuano":"ceb",
    "Esperanto":"eo",
    "Basque":"eu",
    "Irish":"ga"
}
translation_lang["Google"] = {
    "source":dict_google_languages,
    "target":dict_google_languages,
}

dict_bing_languages = {
    "Japanese":"ja",
    "English":"en",
    "Chinese":"zh",
    "Arabic":"ar",
    "Russian":"ru",
    "French":"fr",
    "German":"de",
    "Spanish":"es",
    "Portuguese":"pt",
    "Italian":"it",
    "Korean":"ko",
    "Greek":"el",
    "Dutch":"nl",
    "Hindi":"hi",
    "Turkish":"tr",
    "Malay":"ms",
    "Thai":"th",
    "Vietnamese":"vi",
    "Indonesian":"id",
    "Hebrew":"he",
    "Polish":"pl",
    "Czech":"cs",
    "Hungarian":"hu",
    "Estonian":"et",
    "Bulgarian":"bg",
    "Danish":"da",
    "Finnish":"fi",
    "Romanian":"ro",
    "Swedish":"sv",
    "Slovenian":"sl",
    "Persian/Farsi":"fa",
    "Bosnian":"bs",
    "Serbian":"sr",
    "Fijian":"fj",
    "Filipino":"tl",
    "Haitiancreole":"ht",
    "Catalan":"ca",
    "Croatian":"hr",
    "Latvian":"lv",
    "Lithuanian":"lt",
    "Urdu":"ur",
    "Ukrainian":"uk",
    "Welsh":"cy",
    "Tahiti":"ty",
    "Tongan":"to",
    "Swahili":"sw",
    "Samoan":"sm",
    "Slovak":"sk",
    "Afrikaans":"af",
    "Norwegian":"no",
    "Bengali":"bn",
    "Malagasy":"mg",
    "Maltese":"mt",
    "Queretaro otomi":"otq",
    "Klingon/tlhingan Hol":"tlh",
    "Gujarati":"gu",
    "Tamil":"ta",
    "Telugu":"te",
    "Punjabi":"pa",
    "Irish":"ga"
}
translation_lang["Bing"] = {
    "source":dict_bing_languages,
    "target":dict_bing_languages,
}

dict_ctranslate2_lang = {
    'English': 'en',
    'Chinese': 'zh',
    'German': 'de',
    'Spanish': 'es',
    'Russian': 'ru',
    'Korean': 'ko',
    'French': 'fr',
    'Japanese': 'ja',
    'Portuguese': 'pt',
    'Turkish': 'tr',
    'Polish': 'pl',
    'Catalan': 'ca',
    'Dutch': 'nl',
    'Arabic': 'ar',
    'Swedish': 'sv',
    'Italian': 'it',
    'Indonesian': 'id',
    'Hindi': 'hi',
    'Finnish': 'fi',
    'Vietnamese': 'vi',
    'Hebrew': 'he',
    'Ukrainian': 'uk',
    'Greek': 'el',
    'Malay': 'ms',
    'Czech': 'cs',
    'Romanian': 'ro',
    'Danish': 'da',
    'Hungarian': 'hu',
    'Tamil': 'ta',
    'Norwegian': 'no',
    'Thai': 'th',
    'Urdu': 'ur',
    'Croatian': 'hr',
    'Bulgarian': 'bg',
    'Lithuanian': 'lt',
    'Latin': 'la',
    'Maori': 'mi',
    'Malayalam': 'ml',
    'Welsh': 'cy',
    'Slovak': 'sk',
    'Telugu': 'te',
    'Persian': 'fa',
    'Latvian': 'lv',
    'Bengali': 'bn',
    'Serbian': 'sr',
    'Azerbaijani': 'az',
    'Slovenian': 'sl',
    'Kannada': 'kn',
    'Estonian': 'et',
    'Macedonian': 'mk',
    'Breton': 'br',
    'Basque': 'eu',
    'Icelandic': 'is',
    'Armenian': 'hy',
    'Nepali': 'ne',
    'Mongolian': 'mn',
    'Bosnian': 'bs',
    'Kazakh': 'kk',
    'Albanian': 'sq',
    'Swahili': 'sw',
    'Galician': 'gl',
    'Marathi': 'mr',
    'Punjabi': 'pa',
    'Sinhala': 'si',
    'Khmer': 'km',
    'Shona': 'sn',
    'Yoruba': 'yo',
    'Somali': 'so',
    'Afrikaans': 'af',
    'Occitan': 'oc',
    'Georgian': 'ka',
    'Belarusian': 'be',
    'Tajik': 'tg',
    'Sindhi': 'sd',
    'Gujarati': 'gu',
    'Amharic': 'am',
    'Yiddish': 'yi',
    'Lao': 'lo',
    'Uzbek': 'uz',
    'Faroese': 'fo',
    'Haitian creole': 'ht',
    'Pashto': 'ps',
    'Turkmen': 'tk',
    'Nynorsk': 'nn',
    'Maltese': 'mt',
    'Sanskrit': 'sa',
    'Luxembourgish': 'lb',
    'Myanmar': 'my',
    'Tibetan': 'bo',
    'Tagalog': 'tl',
    'Malagasy': 'mg',
    'Assamese': 'as',
    'Tatar': 'tt',
    'Hawaiian': 'haw',
    'Lingala': 'ln',
    'Hausa': 'ha',
    'Bashkir': 'ba',
    'Javanese': 'jw',
    'Sundanese': 'su'
}

translation_lang["ctranslate2"] = {
    "source":dict_ctranslate2_lang,
    "target":dict_ctranslate2_lang,
}