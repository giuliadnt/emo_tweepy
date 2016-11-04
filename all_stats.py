__author__ = 'GiuliaDnt'

import numpy as np
from preprocessing import *

def main():

    with codecs.open('datafile.json', 'r', encoding='utf32') as f:
        myfile = f.readlines()
    #remove duplicates
    unique = list(set(myfile))
    print '\n'
    print "The length of the original file is: %d tweets" %len(myfile), '\n'
    print "The length of the file with no duplicates is: %d tweets" %len(unique), '\n'
    lengths = np.array([len(i) for i in clean_tweets(unique)])
    mu = np.mean(lengths)
    std = np.std(lengths)
    print "The mean length in the collection of cleaned tweets is: %d characters" %mu, '\n'
    print "The standard deviation is: %d" %std, '\n'
    #more and more
    print "The amount of cleaned tweets with more than 140 characters is: %d" %len([i for i in clean_tweets(unique) if len(i)>140]), '\n'
    print "The amount of cleaned tweets with less than 10 characters is: %d" %len([i for i in clean_tweets(unique) if len(i)<10]), '\n'
    print "Maximum tweet length found is: %d characters" %max([len(i) for i in clean_tweets(unique)]), '\n'
    print "Minimum tweet length found is: %d characters" %min([len(i) for i in clean_tweets(unique)]), '\n'
    print "Removing tweets above 140 characters and below 10 characters...", '\n'
    cleaned = [tweet for tweet in clean_tweets(unique) if len(tweet)<=140 and len(tweet)>=10]
    print "Creating list of keeywords' lists...", '\n'
    key_lists = create_classes_lists(cleaned, keywords)
    print "Creating a triple including a list of pairs (keyword name : num. of instances)...", '\n'
    d, minpair, maxpair = get_name_with_length(key_lists)
    print "The least represented keyword is \"", minpair[0], "\" with %d instances" %minpair[1], '\n'
    print "The best represented keyword is: \"", maxpair[0], "\" with %d instances" %maxpair[1], '\n'
    print "Done!"


if __name__ == '__main__':
    main()

