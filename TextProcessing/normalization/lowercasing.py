from cleantext import clean

def lowercasing(text):
    return clean(text,
    lowercase=True)