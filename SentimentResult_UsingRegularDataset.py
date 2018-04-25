#import Regular and Modified vader libraries
from  nltk.sentiment import SentimentIntensityAnalyzer as vad
from vaderfile import SentimentIntensityAnalyzer as mod
import pandas as pd

#compare both sentiment tools
sentiment = vad()
sentimt = mod()

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
df.to_csv("Regular_SentimentResult_UsingRegularDatset.csv")

#Modified

# result = []
# for row in data:
#      modified = sentimt.polarity_scores(row)
#      if modified['compound'] > 0.5:
#          classification = "Positive"
#      elif -0.5 < modified['compound'] < 0.5:
#          classification = "Neutral"
#      else:
#          classification = "Negative"
#      t=[row, modified['compound'], classification]
#      result.append(t)
#
# headers = ['Text', 'CompoundScore', 'Classification']
# df = pd.DataFrame(result, columns=headers)
# df.to_csv("Modified_SentimentResult1_UsingRegularDataset.csv")