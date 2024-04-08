from fastapi import FastAPI
from pyod.models.knn import KNN   # kNN detector
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

app = FastAPI()

neigh = None
clf = None

@app.on_event("startup")
def load_train_model():
    df = pd.read_csv("iris_ok.csv")
    global neigh
    global clf
    clf = KNN()
    neigh = KNeighborsClassifier(n_neighbors=len(np.unique(df['y'])))
    neigh.fit(df[df.columns[:4]].values.tolist(), df['y'])
    clf.fit(df[df.columns[:4]].values.tolist(), df['y']) 
    print("Model finished the training")

@app.get("/predict")
def predict(p1: float, p2: float, p3: float, p4: float):
    pred = neigh.predict([[p1, p2, p3, p4]])
    return "{}".format(pred[0])

@app.get("/anomaly")
def anomaly(p1: float, p2: float, p3: float, p4: float):
    pred = neigh.predict([[p1, p2, p3, p4]])
    return "{}".format(pred[0])

@app.get("/")
async def root():
    return {"message": "Hello World"}
