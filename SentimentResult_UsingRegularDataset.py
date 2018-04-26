"""This Python file is used for carrying out the regular sentiment analysis
    using the vaderSentiment Library """

#import Regular and Modified vader libraries
from  nltk.sentiment import SentimentIntensityAnalyzer as vad
import pandas as pd

#create vader object
sentiment = vad()

#import file to be analyzed
data = open("Regular_dataset.txt").read().split('\n')

output = []
for row in data:
    regular = sentiment.polarity_scores(row)
    if regular['compound'] > 0.5:
        classification = "Positive"
    elif -0.5 < regular['compound'] < 0.5:
        classification = "Neutral"
    else:
        classification = "Negative"
    t=[row, regular['compound'], classification]
    output.append(t)

headers = ['Text', 'CompoundScore', 'Classification']
df = pd.DataFrame(output, columns=headers)

#specify output location and filename to export data
df.to_csv("csv file")
