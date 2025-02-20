from fastapi import FastAPI
from search_q import search_query

app = FastAPI()

@app.get('/')
def root():
    return {'message': "Hello World"}

@app.get('/search/')
def search(query:str = ''):
    return search_query(query)