"""Helper functions for breaking up text into sentences and words."""

from nltk.tokenize import sent_tokenize, word_tokenize

get_sentences = sent_tokenize

def get_words(string):
    """Extract all words from a string."""
    tokens = word_tokenize(string)
    words = list(filter(lambda x: any(map(str.isalnum, x)), tokens))
    words_lower = list(map(lambda x: x.lower(), words))
    return words_lower
