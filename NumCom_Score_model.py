import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
trainDataframe = trainDataframe[trainDataframe.Flair != -1]


y=trainDataframe["Flair"]
x=trainDataframe[["Score","NumComments"]]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
# print(x.shape())
ss=StandardScaler()
feature = ss.fit_transform(x_train)
print(type(feature))

model = SVC()
model.fit(feature,y_train)

feature_test = ss.fit_transform(x_test)
# print(model.predict(ss.transform([[111,231]])))
print(model.score(feature_test,y_test))

# Saving model and the instance of the scalar

filename_model='Trained_models/NumCom_Score_model.mod'
pickle.dump(model,open(filename_model, 'wb'))
filename_vectorizer='Trained_models/NumCom_Score_scalar.sca'
pickle.dump(ss,open(filename_vectorizer,'wb'))