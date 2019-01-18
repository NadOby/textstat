#!/usr/bin/env python3
# coding: utf-8

import nltk
import re
from collections import Counter


text = open('text.txt', 'r').read()

words_array = nltk.word_tokenize(text)
sentences_list = nltk.sent_tokenize(text)


def words_cleanup(word):
    alfavit = tuple("йцукенгшщзхъфывапролджэячсмитьбюё\
            ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ")

    if word.startswith(alfavit):
        word = re.sub('\.*$', '', word)
        word = re.sub('…$', '', word)

        if '-' in word:
            word = word.split('-')
        elif "\\" in word:
            word = word.split('\\')
        else:
            word = [word]
        return word
    else:
        return []


words_array_filter = []
for x in words_array:
    words_array_filter.extend(words_cleanup(x))

counts = Counter(words_array_filter)
freq = []
for k, v in counts.most_common():
    freq.append("{} {}".format(k, v))

with open('frequencies.txt', mode='wt', encoding='utf-8') as fq:
    fq.write('\n'.join(freq))
    fq.close()

stemmer = nltk.stem.snowball.RussianStemmer()
stem_list = [stemmer.stem(w) for w in words_array_filter]

words_count = len(words_array_filter)

words_uniq = sorted(set(words_array_filter))
words_uniq_count = len(words_uniq)

stems_uniq = sorted(set(stem_list))
stems_uniq_count = len(stems_uniq)

with open('word_list.txt', mode='wt', encoding='utf-8') as wl:
    wl.write('\n'.join(words_uniq))
    wl.close()

with open('stem_list.txt', mode='wt', encoding='utf-8') as sl:
    sl.write('\n'.join(stems_uniq))
    sl.close()

print("Tokens: %d" % len(words_array))
print("Words only: %d" % len(words_array_filter))
print("Unique words: %d" % words_uniq_count)
print("Unique stems: %d" % stems_uniq_count)
