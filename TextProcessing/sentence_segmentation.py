import spacy
import nltk


def sentence_segmentation(text, language='english', NLTK=False):
    sentences = []

    if NLTK:
        sentences = nltk.sent_tokenize(text)
    else:
        if language == 'english':
            nlp = spacy.load('en_core_web_sm', disable=['tagger', 'ner'])
        elif language == 'portuguese':
            nlp = spacy.load('pt_core_news_sm', disable=['tagger', 'ner'])

        if len(text) > 500000:
            ListOfChunks = chunks(text, 500000)
            for chunk in ListOfChunks:
                doc = nlp(chunk)

                for sent in doc.sents:
                    sentences.append(sent.text)
        else:
            doc = nlp(text)

            for sent in doc.sents:
                sentences.append(sent.text)

    return sentences


def chunks(text, n):
    ListOfChunks = []

    """successive n-sized chunks from l."""
    for i in range(0, len(text), n):
        ListOfChunks.append(text[i:i + n])

    return ListOfChunks