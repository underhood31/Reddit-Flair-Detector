import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# Loading the train dataset
trainDataframe = pd.read_csv("./Bert_data/test.tsv", delimiter="\t")
print(trainDataframe.head())
trainDataframe = trainDataframe[trainDataframe.Flair == 1 || trainDataframe.Flair == 8 || trainDataframe.Flair == 11 ]

flairList = trainDataframe["label"]
titleList = trainDataframe["text"]

eighty = int(0.8*len(flairList))

trainFlair=flairList[:eighty]
trainTitle=titleList[:eighty]
testFlair=flairList[eighty:]
testTitle=titleList[eighty:]

cntVectrzr = CountVectorizer()
titleFeatures = cntVectrzr.fit_transform(trainTitle)

model = svm.SVC()
model.fit(titleFeatures,trainFlair)

titleFeaturesTest = cntVectrzr.fit_transform(testTitle)

print(model.score(titleFeatures,trainFlair))


# Testing accuracy of model
# model.score(titleFeaturesTest,flairListTest)
