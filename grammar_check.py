import enchant


def get_grammar_score(text_tokens):
    database = enchant.Dict('ru_RU')
    correct_words_num = 0
    for word in text_tokens:
        correct_words_num += int(database.check(word))
    res = correct_words_num / len(text_tokens)
    return res


if __name__ == '__main__':
    from tokenize_data import proccess_text
    import time

    t0 = time.time()
    text = 'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культурыДобрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры' \
           'Добрый вечир, дамы и господа, рад приветствовать ваз на нашем благотварительном вечери семантических деятелей культуры'
    text_tokens = proccess_text(text, normal_form=True)
    print('grammar rate is  ', get_grammar_score(text_tokens))
    print('time per word is:  ', (time.time() - t0) / len(text_tokens))
