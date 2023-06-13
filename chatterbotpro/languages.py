class BaseLanguage:
    """ This is the base class for all languages. """
    ISO_639_1 = None
    ISO_639 = None
    ENGLISH_NAME = None
    MODEL = None
    GENDER = {}
    PERSON = {}
    PERSON2 = {}
    NORMAL = {}


class ENG(BaseLanguage):
    ISO_639_1 = 'en'
    ISO_639 = 'eng'
    ENGLISH_NAME = 'English'
    MODEL = 'en_core_web_sm'


class POR(BaseLanguage):
    ISO_639_1 = 'pt'
    ISO_639 = 'por'
    ENGLISH_NAME = 'Portuguese'
    MODEL = "pt_core_news_lg"

    GENDER = {
        # masculine -> feminine
        "ele": "ela",
        "dele": "ela",
        "ele mesmo": "ela mesma",

        # feminine -> masculine
        "ela": "ele",
        "dela": "dele",
        "ela mesma": "ele mesmo",
    }

    PERSON = {
        # 1st->3rd (masculine)
        "eu": "ele",
        "meu": "dele",
        "eu mesmo": "ele mesmo",

        # 3rd->1st (masculine)
        "ele": "eu",
        "dele": "meu",
        "ele mesmo": "eu mesmo",

        # 3rd->1st (feminine)
        "ela": "eu",
        "dela": "meu",
        "ela mesma": "eu mesmo",
    }

    PERSON2 = {
        # 1st -> 2nd
        "eu": "você",
        "meu": "seu",
        "eu mesmo": "você mesmo",

        # 2nd -> 1st
        "você": "eu",
        "seu": "meu",
        "você mesmo": "eu mesmo",
    }

    NORMAL = {
        # de -> para
        'vc': 'voce',
        'nudez': 'nude',
        'pv': 'privado',
        'pvd': 'privado',
        'obg': 'obrigado',
        'brigado': 'obrigado',
        'ond': 'onde',
        'aonde': 'onde',
        'zap': 'whatsapp',
        'wpp': 'whatsapp',
        'wts': 'whatsapp',
        'ft': 'foto',
        'peitos': 'tetas',
        'peito': 'tetas',
        'teta': 'tetas',
        'tc': 'fala',
        'vamo': 'vamos',
        'foda-se': 'fodase',
        'fds': 'fodase',
        'nois': 'nos',
        'cmg': 'comigo',
        'vai se foder': 'vsf',
        'vsfd': 'vsf',
        'to': 'estou',
        'ta': 'esta',
        'qui': 'que',
        'q': 'que',
        'es': 'voce é',
        'o que': 'oq',
        'oque': 'oq',
    }
