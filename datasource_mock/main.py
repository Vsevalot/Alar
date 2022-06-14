import json
from typing import TypedDict
from pathlib import Path

from fastapi import FastAPI, Request
from pydantic import BaseModel

import settings


class DataItem(TypedDict):
    id: int
    name: str


app = FastAPI()
app.datasource_path = settings.PATH_TO_DATA
def get_data(self) -> list[DataItem]:
    path_to_data = Path(self.datasource_path)
    print(path_to_data)
    if not path_to_data.exists():
        return []

    with open(path_to_data, 'r') as f:
        data = json.load(f)
        return data['data']
app.get_data = lambda: get_data(app)


class Item(BaseModel):
    id: int
    name: str


class DataResponse(BaseModel):
    result: list[Item]


@app.get("/get_data")
async def root(request: Request):
    data = request.app.get_data()
    return DataResponse(result=data)
