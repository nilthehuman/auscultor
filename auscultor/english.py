# A few helpers specific to the English language

from itertools import chain
from nltk.tokenize import word_tokenize

english_alphabet = [chr(x) for x in chain(range(ord('A'), ord('Z')+1), range(ord('a'), ord('z')+1))]

arabic_numerals = [str(x) for x in range(0, 10)]

whitespace = [' ', '\n', '\r', '\t']

punctuation = [',', '(', ')', '[', ']', '"', '\'', ':', ';', '.', '!', '?']

english_charset = english_alphabet + arabic_numerals + whitespace + punctuation

def non_english_characters(string):
    """Remove all valid Latin characters and symbols from a string."""
    to_remove = str.maketrans(dict.fromkeys(english_charset))
    return string.translate(to_remove)

def prevalence_of_english_charset(string):
    """Determine the ratio of valid Latin characters and symbols in a string (between 0 and 1)."""
    remaining_char_count = len(non_english_characters(string))
    total_char_count = len(string)
    return 1 - remaining_char_count / total_char_count

# Word roots from en.wikipedia.org/wiki/Most_common_words_in_English, inflected forms added by hand.
# Sorted items by category and meaning to make the whole list more readable. Order does not matter.
# Removed the following items: 'day', 'first', 'good', 'new', 'only', 'people', 'time', 'two',
#                              'way', 'work', 'year'.
# Added the following new items: 'before', 'down, 'few', 'here', 'many', 'those', 'though', 'under',
#                                'where', 'whom', 'whose', 'why'.
common_non_verbs = [
    # articles
    'the', 'a', 'an',
    # demonstratives and 'other' (a similar determiner)
    'this', 'that', 'these', 'those', 'other',
    # prepositions
    'from', 'to', 'of', 'for', 'in', 'into', 'out', 'on', 'up', 'down', 'at', 'after', 'before',
    'over', 'under', 'as', 'by', 'with', 'because', 'about',
    # interrogatives
    'what', 'who', 'whom', 'whose', 'which', 'when', 'where', 'how', 'why',
    # conjunctions
    'and', 'or', 'so', 'but', 'though', 'if', 'then', 'than',
    # adverbs
    'no', 'not', 'now', 'here', 'there', 'also', 'just', 'back', 'even', 'well',
    # numerals and quantifiers
    'one', 'all', 'any', 'most', 'some', 'many', 'few',
    # personal and possessive pronouns
    'I', 'me', 'my', 'mine', 'you', 'your', 'yours',
    'it', 'its', 'he', 'him', 'his', 'she', 'her', 'hers',
    'we', 'us', 'our', 'ours', 'they', 'them', 'their', 'theirs'
]

common_verbs = [
    # verbs
    'be', 'am', 'are', 'is', 'was', 'were', 'being', 'been',
    'have', 'has', 'having', 'had',
    'do', 'does', 'doing', 'did', 'done',
    'will', 'would',
    'get', 'gets', 'getting', 'got', 'gotten',
    'come', 'comes', 'coming', 'came',
    'go', 'goes', 'going', 'went', 'gone',
    'say', 'says', 'saying', 'said',
    'make', 'makes', 'making', 'made',
    'can', 'could', 'able',
    'like', 'likes', 'liking', 'liked',
    'know', 'knows', 'knowing', 'knew', 'known',
    'take', 'takes', 'taking', 'took', 'taken',
    'see', 'sees', 'seeing', 'saw', 'seen',
    'look', 'looks', 'looking', 'looked',
    'think', 'thinks', 'thinking', 'thought',
    'use', 'uses', 'using', 'used',
    'want', 'wants', 'wanting', 'wanted',
    'give', 'gives', 'giving', 'gave', 'given'
]

common_words = common_non_verbs + common_verbs

def preprocess(string):
    return word_tokenize(string.lower())

def strip_common_non_verbs(tokens):
    """Remove the most common non-verb words from a list of tokens."""
    return list(filter(lambda x: x not in common_non_verbs, tokens))

def strip_common_words(tokens):
    """Remove the most common English words from a list of tokens."""
    return list(filter(lambda x: x not in common_words, tokens))

def prevalance_of_common_words(tokens):
    """Determine the ratio of common words in a list of tokens (between 0 and 1)."""
    remaining_token_count = len(strip_common_words(tokens))
    total_token_count = len(tokens)
    return 1 - remaining_token_count / total_token_count

# Ensure no duplicates
assert( len(list(set(common_words))) == len(common_words) )

def is_in_english(string):
    tokens = preprocess(string)
    return 0.9 < prevalence_of_english_charset(string) and 0.2 < prevalance_of_common_words(tokens)

