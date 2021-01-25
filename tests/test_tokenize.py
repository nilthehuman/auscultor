"""Unit tests for splitting text into sentences and words."""

# pylint: disable=missing-function-docstring

import auscultor.tokenize
from .data import UDHR_ARTICLE_1

def test_get_sentences():
    assert len(auscultor.tokenize.get_sentences(UDHR_ARTICLE_1)) == 3

def test_get_words():
    assert len(auscultor.tokenize.get_words(UDHR_ARTICLE_1)) == 32

def test_oxford_join():
    assert auscultor.tokenize.oxford_join(['one']) == 'one'
    assert auscultor.tokenize.oxford_join(['one', 'two']) == 'one and two'
    assert auscultor.tokenize.oxford_join(['one', 'two', 'three']) == 'one, two, and three'
