import pickle

model = pickle.load(open('./Trained_models/title_model.mod','rb'))
cv = pickle.load(open('./Trained_models/title_vectorizer.vec','rb'))
print(model.predict(cv.transform([""])))

print(type(model))
print(type(cv))