"""Unit tests for the module that checks if text is in English."""

# pylint: disable=missing-function-docstring

import auscultor.verify_english

from auscultor.tokenize import get_words
from .data import UDHR_ARTICLE_1

def test_non_english_characters():
    assert auscultor.verify_english.non_english_characters(UDHR_ARTICLE_1) == ""

def test_prevalence_of_english_characters():
    assert auscultor.verify_english.prevalence_of_english_characters(UDHR_ARTICLE_1) == 1

def test_strip_common_non_verbs():
    words = get_words(UDHR_ARTICLE_1)
    assert len(auscultor.verify_english.strip_common_non_verbs(words)) == 20

def test_strip_common_words():
    words = get_words(UDHR_ARTICLE_1)
    assert len(auscultor.verify_english.strip_common_words(words)) == 18

def test_prevalence_of_common_words():
    words = get_words(UDHR_ARTICLE_1)
    assert auscultor.verify_english.prevalence_of_common_words(words) >= 0.4

def test_is_in_english():
    assert auscultor.verify_english.is_in_english(UDHR_ARTICLE_1)
