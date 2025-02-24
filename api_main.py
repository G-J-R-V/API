from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from Models.Kmeans import KMeansGroups
from search_q import json_data_dict
from search_q import search_query


class Item(BaseModel):
    doc_ids: list[int]


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/search/")
def search(query: str = ""):
    if query == "":
        return {"message": "Digite uma pesquisa"}
    query_result = search_query(query)
    if type(query_result) == str:
        raise HTTPException(status_code=404, detail="Item not found")
    return query_result


@app.post("/user_selection/")
def user_selection(item: Item):

    # Get all doc_ids that the user clicked on
    doc_ids = item.doc_ids

    dados = json_data_dict

    for doc_id in doc_ids:
        if doc := dados.get(f"Doc{int(doc_id)-1}"):
            doc["R"] = True

    # print(dados)

    return {"message": "Success"}


@app.get("/kmeans/")
def kmeans():
    return KMeansGroups()
