import csv
import re
import string
from nltk.corpus import stopwords


def standard_words(word):
    remove = string.punctuation
    remove = remove.replace("-", "")  # don't remove hyphens
    pattern = r"[{}]".format(remove)  # create the pattern
    return re.sub(pattern, "", word)


words = set()
word_freq = {}

tags = []
with open("tags.txt", newline='') as all_tags:
    temp = csv.reader(all_tags, delimiter=',')
    for tag in temp:
        tags += tag


def topic_detect(fn):
    topic = set()
    with open(fn, newline='') as afile:
        lines = csv.reader(afile, delimiter='\t')
        for line in lines:
            for word in standard_words(line[3]).split():
                if word not in stopwords.words("english") and word in tags:
                    topic.add(word)

    if topic == []:
        print('No related topics found')
    else:
        print('Topics Detected: ' + ', '.join(topic))


topic_detect('5.tsv')
