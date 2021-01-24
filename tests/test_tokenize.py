"""Unit tests for splitting text into sentences and words."""

# pylint: disable=missing-function-docstring

import auscultor.tokenize
from .data import UDHR_ARTICLE_1

def test_get_sentences():
    assert len(auscultor.tokenize.get_sentences(UDHR_ARTICLE_1)) == 3

def test_get_words():
    assert len(auscultor.tokenize.get_words(UDHR_ARTICLE_1)) == 32
