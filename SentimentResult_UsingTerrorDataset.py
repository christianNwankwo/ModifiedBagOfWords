"""This Python file is used for carrying out the sentiment analysis
    using the Modified lexicon file of the vaderSentiment Library """

#import vader library linked with the modified lexicon file
from vaderfile import SentimentIntensityAnalyzer as mod
import pandas as pd

#create vader object
sentimt = mod()

#import dataset containing terror keywords e.g bomb
filename = ""
path = ""
f = open("filename+path")
data = f.read()

#Modified
result = []
for row in data.split('\n')[1:]:
     modified = sentimt.polarity_scores(row)
     if modified['compound'] > 0.5:
         classification = "Positive"
     elif -0.5 < modified['compound'] < 0.5:
         classification = "Neutral"
     else:
         classification = "Negative"
     t=[row, modified['compound'], classification]
     result.append(t)

headers = ['Text', 'CompoundScore', 'Classification']
df = pd.DataFrame(result, columns=headers)

#specify output location and filename to export data
output_location = ''
filename = ''
df.to_csv("output_location+filename")
