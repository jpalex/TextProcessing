import nltk


def stopwords_removal(text, language="english"):
    ListOfTokens = nltk.word_tokenize(text)
    stopword_list = nltk.corpus.stopwords.words(language)

    filtered_tokens = [token for token in ListOfTokens if token.lower() not in stopword_list]

    filtered_text = ' '.join(filtered_tokens)

    return filtered_text