"""Helper functions for breaking up text into sentences and words."""

from nltk.tokenize import sent_tokenize, word_tokenize

get_sentences = sent_tokenize

def get_words(string):
    """Extract all words from a string."""
    tokens = word_tokenize(string)
    words = list(filter(lambda x: any(map(str.isalnum, x)), tokens))
    return words

def oxford_join(words):
    """Concatenate words with commas and a final 'and' between."""
    assert 0 < len(words)
    if 1 == len(words):
        return words[0]
    elif 2 == len(words):
        return words[0] + ' and ' + words[1]
    else:
        return ' '.join(map(lambda x: x + ',', words[0:-1])) + ' and ' + words[-1]
