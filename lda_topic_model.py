from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import os
import csv

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print (" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

documents = []
for fn in os.listdir('4/'):
    with open('4/%s'%fn, newline='') as afile:
        lines = csv.reader(afile, delimiter='\t')
        for line in lines:
            documents.append(line[3])

no_features = 1000
no_topics = 50
no_top_words = 5

# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tf = tf_vectorizer.fit_transform(documents)
tf_feature_names = tf_vectorizer.get_feature_names()
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

display_topics(lda, tf_feature_names, no_top_words)

import pickle
with open('lda_model.pkl', 'wb') as fout:
  pickle.dump((tf_vectorizer, lda), fout)
