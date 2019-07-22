# Reddit-Flair-Detector

## Python(3.7) Dependencies:
###	praw
###	pandas
###	pymongo
###	datetime
###	csv
###	sklearn
###	collections
###	flask
### gunicorn (works only on unix like os)
## JS libraries used:
###	c3.js
###	chart.js
## Scripts:
###	redditConnect.py--> Scrap reddit data and put it into local instance of mongoDB into two collections named, test and train
###	process_data.py--> Takes data from mongoDB collections and process data in a way which can be fed to the machine learing models and save it in Processed_Data/all.csv and Webapp/Data/all.csv. For number coding, read Processed_Data/readme.txt
###	comment_model.py--> Predicts using comments and save model in /Trained_models. RandomForestClassifier used.
###	title_model.py--> Predicts using title and save model in /Trained_models. RandomForestClassifier used.
###	NumCom_Score_model.py--> Predicts using no. of comments and score and save model in /Trained_models. SVC used.
###	numComments_model.py--> Predicts using no. of comments and save model in /Trained_models. SVC used.
###	score_model.py--> Predicts using scores and save model in /Trained_models. SVC used.
### use_model.py--> use title_model to predict results
## Usage:
### execute the scripts in the order above
### For predicting use use_model.py
## Webapp (https://reddit-flair-detector-precog.herokuapp.com/)
### Code in /Webapp folder. Is is a flask app
### Hosted in heroku
### To run on localhost, run *<code>gunicorn index:app</code>* in /Webapp directory
### Flair is predicted using title_model
## Help from:
###	http://www.storybench.org/how-to-scrape-reddit-with-python/
###	https://praw.readthedocs.io/en/latest/index.html
###	https://appliedmachinelearning.blog/2019/03/04/state-of-the-art-text-classification-using-bert-model-predict-the-happiness-hackerearth-challenge/
###	stackoverflow
###	https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
###	https://github.com/huyle333/graphs-from-csv
### https://developers.google.com/chart/interactive/docs/gallery/histogram
### https://medium.com/@aneesha/svm-parameter-tuning-in-scikit-learn-using-gridsearchcv-2413c02125a0
### https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
### https://c3js.org/
### https://medium.com/@taplapinger/tuning-a-random-forest-classifier-1b252d1dde92
### https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
