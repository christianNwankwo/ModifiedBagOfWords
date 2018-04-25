#import necessary txt files

vader= open("vader_lexicon.txt")
terror= open("terror.txt")
doc = open("New_lexicon.txt", 'w')
pos = open('positive.txt').read()
verb = [i for i in open("verbs.txt").read().split(',')]
pos_list = [v for v in pos.split()]
check = []


import pandas as pd
data = pd.read_csv('WordCount.csv')
words = data['Word']
for value in words[0:1000]:
    if value not in pos_list and len(value) > 3 and value not in verb:
        check.append(value)
#         doc.write(value + "\t" + "\t-50000000.0\t0.0\t[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4]".strip())
#         doc.write("\n")
# doc.close()
