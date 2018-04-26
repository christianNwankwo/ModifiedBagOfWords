""" This python file is used for Natural Language Processing by calculating the number of occurence of each word in the
    RAND Database of Worldwide Terrorism Incidents file. """

import string, pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#remove countries from text...
re_country = [row.split('.', 1)[1:] for row in col]

#import dataset as pandas object
filepath = pd.read_csv("Enter filename + path here")

#select the text column
column = filepath['Description']

#set stopwords and punctuation
stopwords = set(stopwords.words('english'))
exclude = set(string.punctuation)
#change sentence case to lower
file_lower = [row.lower() for row in column]
#tokenize words
tokens = [word_tokenize(r) for r in file_lower]
#remove stopwords
no_stopword = [v for s in tokens for v in s if v not in stopwords]
#remove punctuation
no_punc = ','.join([v for v in no_stopword if v not in exclude])

#define word count
def count(data):
    words = data.split(',')
    total = {}

    for word in words:
        if word in total:
            total[word] += 1
        else:
            total[word] = 1
    return total

#apply word count
count = (count(no_punc))
#convert dictionary to pandas DataFrame
data = pd.DataFrame(list(count.items()), columns=["Word", "Count"])
#sort DataFrame
dataset = data.sort_values("Count", ascending=False)
#export to csv
dataset.to_csv("Enter filename + path here")
