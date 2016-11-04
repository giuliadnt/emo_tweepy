__author__ = 'GiuliaDnt'


#SOME BASIC DATA ANALYSIS AND PREPROCESSING FOR ANNOTATION
#TODO: (ML PART)
#tokenize
#remove punctuation ?
#retweets handle or not?

import codecs
import re
import numpy as np

#use this list to keep only tweets containing emoji
keywords = [u'\U0001F3F0', u'\U0001F3EB', u'\U0001F3E1', #places
            u'\U00002615', u'\U0001F355',u'\U0001F369',  #food&drinks
            u'\U0001F3C0', u'\U0001F3C6', u'\U0001F3CA', #sport
            u'\U0001F3A4 ',u'\U0001F3B8', u'\U0001F3B6', #music
            u'\U0001F3A8', u'\U0001F4FA', u'\U0001F4DA', #other activities
            u'\U0001F436', u'\U0001F341 ', u'\U00002744', #nature&animals
            u'\U0001F393', u'\U0001F389',u'\U0001F383',   #events
            u'\U0001F46B', u'\U0001F64B', u'\U0001F6B6',  #people
            u'\U0001F622',u'\U0001F612', u'\U0001F60D',   #feelings
            u'\U00002708 ', u'\U0001F697', u'\U000026F5' ] #traveling

keywords_names = ["european castle", "school", "home + garden",
                  "hot beverage", "pizza", "doughnut",
                  "basketball and hoop", "trophy", "swimmer",
                  "microphone", "guitar", "musical notes",
                  "artist palette", "television", "books",
                  "dog", "maple leaf", "snowflake",
                  "graduation cap", "party popper", "jack-o-lantern",
                  "man and woman holding hands", "person raising one hand", "person walking",
                  "crying face", "unamused face", "smiling face with heart eyes",
                  "airplane", "car", "sailboat"]


def clean_tweets(list_of_tweets):
    """
    :param list_of_tweets: list of unique tweets (no duplicates)
    :return: list of preprocessed tweets
    the function standardizes mentions --> @USER
    and URLs --> @URL
    removes BOM character
    """
    #PATTERNS
    #matches @username
    mentions =re.compile('(@.*?)(?=\s|\:)')#(^|\s)
    #matches URLs, regex from stackoverflow
    #http://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string
    links =re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')

    no_mentions = [re.sub(mentions, "@USER", i) for i in list_of_tweets]
    no_links = [re.sub(links, "@URL", i) for i in no_mentions]
    no_BOM = [re.sub(u"\ufeff", "", i) for i in no_links]
    no_newlinechar = [re.sub('\n',"", i) for i in no_BOM]
    return no_newlinechar


def create_classes_lists(list2, keywords_list):
    """
    :param list2: list without duplicates
    :param keywords_list: list of emoji keywords
    :return: list of lists, each list contains tweets extracted by means of a specific keyword
    """
    return [[i for i in list2 if keywords_list[num] in i] for num in range(len(keywords_list))]

def get_name_with_length(mylist):
    """
    :param mylist: list of lists (each list correspond to a keyword
    :return: triple
             1st item: keyword name and num of items of the shortest list
             2nd item: keyword name and num of items of the longest list
             3rd item:
    """
    lengths = [len(lists) for lists in mylist]
    d = [(keywords_names[idx], i) for idx, i in enumerate(lengths)]
    min_pair =  min(d, key=lambda x: x[1])
    max_pair =  max(d, key=lambda x: x[1])
    return d, min_pair, max_pair


with codecs.open('datafile.json', 'r', encoding='utf32') as f:
     myfile = f.readlines()
#remove duplicates
unique = list(set(myfile))
cleaned = [tweet for tweet in clean_tweets(unique) if len(tweet)<=140 and len(tweet)>=10]
key_lists = create_classes_lists(cleaned, keywords)





