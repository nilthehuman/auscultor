from auscultor.english import prevalence_of_english_charset, is_in_english

udhr_article_1 = ("Article 1.\n"
    "All human beings are born free and equal in dignity and rights.\n"
    "They are endowed with reason and conscience and should\n"
    "act towards one another in a spirit of brotherhood.")

def test_prevalence_of_english_charset():
    assert prevalence_of_english_charset(udhr_article_1) == 1

def test_is_in_english():
    assert is_in_english(udhr_article_1) == True
