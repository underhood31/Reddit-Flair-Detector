import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
trainDataframe = trainDataframe[trainDataframe.Flair != -1]

y=trainDataframe["Flair"]
x=trainDataframe["NumComments"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
features = np.array(x_train)

model = svm.SVC()
model.fit(features.reshape(-1,1),y_train)
features_test = np.array(x_test)
# print(model.predict(np.array([1]).reshape(-1,1)))
# print(model.predict_proba(features_test[8]))
print(model.score(features_test.reshape(-1,1),y_test))

# Saving the model
filename_model='Trained_models/numComments_model.mod'
pickle.dump(model,open(filename_model, 'wb'))
