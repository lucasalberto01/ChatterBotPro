import string
from chatterbotpro import languages


class LowercaseTagger(object):
    """
    Returns the text in lowercase.
    """

    def __init__(self, language=None):
        self.language = language or languages.POR

    def get_text_index_string(self, text: str):
        return text.lower()


class PosLemmaTagger(object):
    """
    Returns a string of text containing part-of-speech, lemma pairs.
    """

    def __init__(self, language=None):
        import spacy

        self.language = language or languages.POR

        self.punctuation_table = str.maketrans(dict.fromkeys(string.punctuation))

        self.nlp = spacy.load(self.language.MODEL)

    def get_text_index_string(self, text: str):
        """
        Return a string of text containing part-of-speech, lemma pairs.
        """
        bigram_pairs = []

        if len(text) <= 2:
            text_without_punctuation = text.translate(self.punctuation_table)
            if len(text_without_punctuation) >= 1:
                text = text_without_punctuation

        document = self.nlp(text)

        if len(text) <= 2:
            bigram_pairs = [
                token.lemma_.lower() for token in document
            ]
        else:
            tokens = [
                token for token in document if token.is_alpha and not token.is_stop
            ]

            if len(tokens) < 2:
                tokens = [
                    token for token in document if token.is_alpha
                ]

            for index in range(1, len(tokens)):
                bigram_pairs.append('{}:{}'.format(
                    tokens[index - 1].pos_,
                    tokens[index].lemma_.lower()
                ))

        if not bigram_pairs:
            bigram_pairs = [
                token.lemma_.lower() for token in document
            ]

        return ' '.join(bigram_pairs)
