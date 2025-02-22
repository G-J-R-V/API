from fastapi import FastAPI
from search_q import search_query
from Models.Kmeans import ModifyJson

app = FastAPI()

@app.get('/')
def root():
    return {'message': "Hello World"}

@app.get('/kmeans/')
def kmeans():
    return ModifyJson()

@app.get('/search/')
def search(query:str = ''):
    return search_query(query)