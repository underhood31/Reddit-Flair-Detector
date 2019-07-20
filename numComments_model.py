import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB

trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
# # print(trainDataframe.describe())
# trainDataframe1 = trainDataframe[trainDataframe.Flair == 1]
# trainDataframe2 = trainDataframe[trainDataframe.Flair == 8]
# trainDataframe3 = trainDataframe[trainDataframe.Flair == 11]


# y=pd.get_dummies(trainDataframe["Flair"])
# z=pd.concat([trainDataframe1,trainDataframe2,trainDataframe3])
y=trainDataframe["Flair"]
print(type(y))
x=trainDataframe["NumComments"]
print(trainDataframe.Text.values[0])
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
# print(len(x_test),len(x_train),len(y_test),len(y_train))
cv=TfidfVectorizer()
features = np.array(x_train)
# print(type(features))

model = svm.SVC()
model.fit(features.reshape(-1,1),y_train)
# print(model.best_params_)
features_test = np.array(x_test)
print(model.predict(features_test[8]))
print(model.predict_proba(features_test[8]))
print(model.score(features_test.reshape(-1,1),y_test))