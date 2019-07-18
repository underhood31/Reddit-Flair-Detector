import pymongo as pm
import csv 
# DB configurations
client = pm.MongoClient('localhost', 27017)
db = client['reddit_data']
Test = db['test']
Train = db['train']

with open('./Data/Test.tsv', 'w', encoding='utf-8',newline='') as testData:  
    w = csv.DictWriter(testData, Test.find_one().keys(), delimiter ='\t')
    w.writeheader()
    for d in Test.find():
        w.writerow(d)
        
with open('./Data/Train.tsv', 'w', encoding='utf-8',newline='') as trainData: 
    w = csv.DictWriter(trainData, Train.find_one().keys(), delimiter ='\t')
    w.writeheader()
    for d in Train.find():
        w.writerow(d)
        
with open('./Data/all.tsv', 'w', encoding='utf-8',newline='') as allData: 
    w = csv.DictWriter(allData, Train.find_one().keys(), delimiter ='\t')
    w.writeheader()
    for d in Train.find():
        w.writerow(d)
    for d in Test.find():
        w.writerow(d)
        