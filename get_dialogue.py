import csv
import os
import re
import string
from collections import Counter
from nltk.corpus import stopwords


def standard_words(word):
    remove = string.punctuation
    remove = remove.replace("-", "")  # don't remove hyphens
    pattern = r"[{}]".format(remove)  # create the pattern
    return re.sub(pattern, "", word)


words = set()
word_freq = {}
# get word frequency in all dialogues

for fn in os.listdir('sampledata'):
    with open('sampledata/%s' % fn, newline='') as afile:
        lines = csv.reader(afile, delimiter='\t')
        for line in lines:
            for word in standard_words(line[3]).split():
                if word not in stopwords.words("english"):
                    words.add(word.lower())
                    if not word_freq.get(word):
                        word_freq[word] = 1
                    else:
                        word_freq[word] += 1
print(word_freq)

tags = []
with open("tags.txt", newline='') as all_tags:
    temp = csv.reader(all_tags, delimiter=',')
    for tag in temp:
        tags += tag

tags = tags[:]

d = Counter(word_freq)

ord = d.most_common()
print(ord)
print(tags)

count = 0
res = []
for ele in ord:
    while count < 10:
        if ele[0] in tags:
            res.append((ele[0], ele[1]))
            count += 1
        break
print(res)
