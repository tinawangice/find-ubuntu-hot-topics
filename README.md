# Find most popular topics from chat dialogues & Topic detector

## Find most popular topics

### Dataset:

Ubuntu OS from the Ubuntu dialog data located at  http://dataset.cs.mcgill.ca/ubuntu-corpus-1.0/

### get_dialogue.py

This script parsed the dialogue data and count the frequncies of each word.

### tag.py

Select tags used together with Ubuntu from Stackoverflow.com tags collection, which can be found: https://github.com/dgrtwo/StackLite

### topic_detector.py

Find the most frequent ten words from dialogues, which can also be found in stackoverflow tags.

Results: [('ubuntu', 72185), ('install', 58638), ('get', 42365), ('using', 27031), ('sudo', 25845), ('file', 25557), ('windows', 21849), ('run', 20328), ('linux', 19067), ('make', 17821)]


## Topic detect and generate relevant topics

### lda_topic_model.py

Train lda model to generate topics based on word frequencey.









