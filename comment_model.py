import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
trainDataframe1 = trainDataframe[trainDataframe.Flair != -1]

y=trainDataframe["Flair"]
x=trainDataframe["Comments"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
cv=CountVectorizer()
features = cv.fit_transform(x_train)
model = RandomForestClassifier(
    class_weight="balanced",
    n_estimators=150
)
model.fit(features,y_train)

features_test = cv.transform(x_test)
# print(y_train.head())
# print(model.predict(features_test[1]))
# print(model.predict_proba(features_test[1]))
print(model.score(features_test,y_test))

# Saving model and the instance of the vectorizer

filename_model='Trained_models/comment_model.mod'
pickle.dump(model,open(filename_model, 'wb'))
filename_vectorizer='Trained_models/comment_vectorizer.vec'
pickle.dump(cv,open(filename_vectorizer,'wb'))