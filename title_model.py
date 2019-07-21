import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.externals import joblib
trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
trainDataframe1 = trainDataframe[trainDataframe.Flair != -1]

y=trainDataframe["Flair"]
x=trainDataframe["Text"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
cv=CountVectorizer()
features = cv.fit_transform(x_train)
model = RandomForestClassifier(
    # class_weight="balanced",
    n_estimators=150
)
model.fit(features,y_train)

features_test = cv.transform(x_test)
# print(y_train.head())
# print(model.predict(cv.transform(["weekly mental health support thread july 21 2019"])))
# print(model.predict_proba("weekly mental health support thread july 21 2019"))
print(model.score(features_test,y_test))

#Saving model

filename_model='Trained_models/title_model.mod'
forWebapp_model = 'Webapp/model/title_model.mod'
pickle.dump(model,open(filename_model, 'wb'))
pickle.dump(model,open(forWebapp_model, 'wb'))
filename_vectorizer='Trained_models/title_vectorizer.vec'
forWebapp_vectorizer = 'Webapp/model/title_vectorizer.vec'
pickle.dump(cv,open(filename_vectorizer,'wb'))
pickle.dump(cv,open(forWebapp_vectorizer,'wb'))
