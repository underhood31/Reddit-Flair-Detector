import pandas as pd
import nltk
import gensim
import numpy as np
import numpy
from gensim import corpora, models, similarities

df = pd.read_csv("./Bert_data/test.tsv", delimiter="\t")
corpus=df["text"].values.tolist()
tol_corp = [nltk.word_tokenize(sent) for sent in corpus]

model = gensim.models.Word2Vec(tol_corp,min_count=1,size=32)
print(type(model['hi']))
print(model.most_similar("Just one word, can we get those days again!"))
print(model.most_similar("I painted my uncle yesterday. I'm on my trip here in Punjab and have been trying to create this for years now. Oil in sketchbook"))
