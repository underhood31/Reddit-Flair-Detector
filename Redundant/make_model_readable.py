from nltk.tokenize import sent_tokenize, word_tokenize 

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from pandas import DataFrame
 
def getLabel(s):

    flairToInt = {
        "Other": -1,
        "AMA":0,
        "AMA Concluded":0,
        "Casual AMA":0,
        "AskIndia":1,
        "Business/Finance":2,
        "Demonetization":3,
        "Entertainment":4,
        "Food":5,
        "Lifehacks":6,
        "Misleading":7,
        "Non-Political":8,
        "Photography":9,
        "Policy":10,
        "Policy & Economy":10,
        "Policy/Economy":10,
        "Politics":11,
        "Politics -- Source in comments": 11,
        "Politics [OLD]":11,
        "Scheduled":12,
        "Science & Technology":13,
        "Science/Technology":13,
        "Sports":14,
        "[R]eddiquette":15,
        "r/all":16,
        "/r/all":17 
    }
    toReturn=[]
    for i in s:
        try:
            temp = flairToInt[i]
            toReturn.append(temp)
        except KeyError:
            toReturn.append(-1)            
    return toReturn

trainDataframe = pd.read_csv("Data/train.tsv", delimiter="\t")
 
# Creating train and dev dataframes according to BERT
dataframeForBert = pd.DataFrame({'user_id':trainDataframe['Username'],
            'label':getLabel(trainDataframe['Flair']),
            'text':trainDataframe['Title'].replace(r'\n',' ',regex=True)})
 
df_bert_train, df_bert_dev = train_test_split(dataframeForBert, test_size=0.01)
 
# Creating test dataframe according to BERT
testDataframe = pd.read_csv("Data/test.tsv", delimiter="\t")
df_bert_test = pd.DataFrame({'user_id':testDataframe['Username'],
                            'label':getLabel(testDataframe['Flair']),
                             'text':testDataframe['Title'].replace(r'\n',' ',regex=True)})
 
# Saving dataframes to .tsv format as required by BERT
df_bert_train.to_csv('Bert_data/train.csv', sep='\t', index=False, header=True)
df_bert_dev.to_csv('Bert_data/dev.csv', sep='\t', index=False, header=True)
df_bert_test.to_csv('Bert_data/test.csv', sep='\t', index=False, header=True)