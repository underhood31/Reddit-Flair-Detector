import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import StandardScaler

trainDataframe = pd.read_csv("./Processed_Data/all.csv", delimiter="\t")
# # print(trainDataframe.describe())
# trainDataframe1 = trainDataframe[trainDataframe.Flair == 1]
# trainDataframe2 = trainDataframe[trainDataframe.Flair == 8]
# trainDataframe3 = trainDataframe[trainDataframe.Flair == 11]


# y=pd.get_dummies(trainDataframe["Flair"])
# z=pd.concat([trainDataframe1,trainDataframe2,trainDataframe3])
y=trainDataframe["Flair"]
print(type(y))
x=trainDataframe[["Score","NumComments"]]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
# print(x.shape())
ss=StandardScaler()
feature = ss.fit_transform(x_train)
print(type(feature))

model = SVC()
model.fit(feature,y_train)
# # print(model.best_params_)
# features_test1 = np.array(x1_test)
# features_test2 = np.array(x2_test)
feature_test = ss.fit_transform(x_test)
print(model.score(feature_test,y_test))