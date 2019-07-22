import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
import string
import pymongo as pm
def FlairToNum(s):

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
        "/r/all":16
    }
    toReturn=[]
    for i in s:
        try:
            temp = flairToInt[i]
            toReturn.append(temp)
        except KeyError:
            toReturn.append(-1)            
    return toReturn

def CategoryToNum(s):
    categoryToInt = {
       'Top':1,
       'New':2,
       'Controversial':3,
       'Rising':4,
       'Hot':5
    }
    toReturn=[]
    for i in s:
        try:
            temp = categoryToInt[i]
            toReturn.append(temp)
        except KeyError:
            toReturn.append(-1)            
    return toReturn

def getTheHour(s):
    toReturn =[]
    for i in s:
        i=str(i)
        i=i.split()[1] #for getting the time
        i=float(i.split(":")[0]) #to Get the hour
        toReturn.append(i)
    return toReturn
def simplifyText(s):
    toRet=[]
    for i in s:
        for c in string.punctuation:
            i= i.replace(c," ")
            i=i.lower()
        toRet.append(i)
    return toRet

# DB configurations
client = pm.MongoClient('localhost', 27017)
db = client['reddit_data']
Test = db['test']
Train = db['train']

data = {}
for i in  Test.find()[0]:
    data[i]=[] 

for d in Test.find():
    for i in d.keys():
        data[i].append(str(d[i]))

for d in Train.find():
    for i in d.keys():
        data[i].append(str(d[i]))


# print(data['Flair'])



# data = pd.read_csv("Data/all.tsv", delimiter="\t")

# Creating train and dev dataframes according to BERT
numDF = pd.DataFrame({'UserId':data['Username'],
            'Category': CategoryToNum(data['Category']),
            'Flair':FlairToNum(data['Flair']),
            'Score':data['Score'],
            'NumComments': data['NoOfComments'],
            'Hour': getTheHour(data['TimeStamp']),
            'Text':simplifyText(data['Title']),
            'Comments':simplifyText(data['Comments'])
            })
 
numDF.to_csv('Processed_Data/all.csv', sep='\t', index=False, header=True)
numDF.to_csv('Webapp/Data/all.csv', sep='\t', index=False, header=True)
