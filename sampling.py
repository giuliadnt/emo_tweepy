import codecs
import json
import random

from preprocessing import *

with codecs.open('datafile.json', 'r', encoding='utf32') as f:
     myfile = f.readlines()

#remove duplicates
unique = list(set(myfile))
cleaned = [tweet for tweet in clean_tweets(unique) if len(tweet)<=140 and len(tweet)>=10]
key_lists = create_keywords_lists(cleaned, keywords)

tuples = [[[re.sub(keywords[index], '<KEY_EMOJI>', tweet), keywords[index]] for tweet in l ]  for index, l in enumerate(key_lists)]


classes = group_keywords_by_class(tuples, 3)

#SAMPLE DATA FOR ANNOTATION, LOWER BOUND (920) --> NUMBER OF INSTANCES IN LEAST POPULATED CLASS

random.seed(5)

#RANDOM INDICES, 920 ITEM PER CLASS

rand_ind = [random.sample(xrange(len(i)), 920) for i in classes]

#FLAT LIST OF CLASS SAMPLES FROM ORIGINAL CORPUS
nl = []
for ind, tweet_list in enumerate(classes):
    for indd, ind_list in enumerate(rand_ind):
        if ind == indd:
            for index in ind_list:
                nl.append(tweet_list[index])

print len(nl)

'''
NESTED LIST OF CLASS SAMPLES FROM ORIGINAL CORPUS
newlist = [[tweet_list[index] for index in ind_list]
           for ind, tweet_list in enumerate(classes)
           for indd, ind_list in enumerate(rand_ind)
           if ind==indd]

'''

a = ['tweet_text', 'emoji_keyword']

my_json = json.dumps([dict(zip(a, row)) for row in nl], indent=1)

with codecs.open('tweet_pairs.json', 'w', encoding='utf32') as f:
    json.dump([dict(zip(a, row)) for row in nl], f, indent=1)
print my_json
