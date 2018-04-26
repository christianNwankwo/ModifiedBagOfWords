""" This python file is used to select the Top 1000 most occurring words gotten from the terror dataset. These words
    would then be added to the vader lexicon fileself.
    This is the process of modifying the vader lexicon file"""

#import the vader lexicon file, a list of words and positive bag of words.
#The verbs and the positive bow are used to check that we do not append words that don't help improve the results of our analysis
vader= open("vader_lexicon.txt", 'a')
pos = open('positive.txt').read()
pos_list = [v for v in pos.split()]
verb = [i for i in open("verbs.txt").read().split(',')]

#The top 1000 words and collected and appended to the vader lexicon file in the same format
import pandas as pd
data = pd.read_csv('WordCount.csv')
words = data['Word']
for value in words[0:1000]:
    if value not in pos_list and len(value) > 3 and value not in verb:
        vader.write(value + "\t" + "\t-50000000.0\t0.0\t[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4]".strip())
        doc.write("\n")
vader.close()
