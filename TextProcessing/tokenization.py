import spacy
import nltk


def tokenization(text, language='english', NLTK=False):
    ListOfTokens = []

    if NLTK:
        ListOfTokens = nltk.word_tokenize(text)
    else:
        if language == 'english':
            nlp = spacy.load('en_core_web_sm', disable=['tagger', 'parser', 'ner'])
        elif language == 'portuguese':
            nlp = spacy.load('pt_core_news_sm', disable=['tagger', 'parser', 'ner'])

        if len(text) > 500000:
            ListOfChunks = chunks(text, 500000)
            for chunk in ListOfChunks:
                doc = nlp.make_doc(chunk)

                for token in doc:
                    ListOfTokens.append(token.text)
        else:
            doc = nlp.make_doc(text)

            for token in doc:
                ListOfTokens.append(token.text)

    return ListOfTokens


def chunks(text, n):
    ListOfChunks = []

    """successive n-sized chunks from l."""
    for i in range(0, len(text), n):
        ListOfChunks.append(text[i:i + n])

    return ListOfChunks