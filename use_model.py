import pickle
flairToInt = {
        
        "AMA":0,
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
        "Politics":11,
        "Scheduled":12,
        "Science & Technology":13,
        "Sports":14,
        "[R]eddiquette":15,
        "/r/all":16
    }
s=input("Enrter the string to predict: ")
model = pickle.load(open('./Trained_models/title_model.mod','rb'))
cv = pickle.load(open('./Trained_models/title_vectorizer.vec','rb'))
numToFlair = dict(map(reversed, flairToInt.items()))

print(numToFlair[int(model.predict(cv.transform([s]))[0])])

# print(type(model))
# print(type(cv))