import auscultor.verify_english

udhr_article_1 = ("Article 1.\n"
    "All human beings are born free and equal in dignity and rights.\n"
    "They are endowed with reason and conscience and should\n"
    "act towards one another in a spirit of brotherhood.")

def test_non_english_characters():
    assert auscultor.verify_english.non_english_characters(udhr_article_1) == ""

def test_prevalence_of_english_characters():
    assert auscultor.verify_english.prevalence_of_english_characters(udhr_article_1) == 1

def test_is_in_english():
    assert auscultor.verify_english.is_in_english(udhr_article_1) == True
