import json
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

import settings
import time


class Item(BaseModel):
    id: int
    name: str


class DataResponse(BaseModel):
    result: list[Item]


def get_data(path_to_data: str) -> list[Item]:
    path_to_data = Path(path_to_data)
    if not path_to_data.exists():
        return []

    with open(path_to_data, 'r') as f:
        data = json.load(f)
        return data['data']


app = FastAPI()

@app.get("/get_data")
async def root() -> DataResponse:
    time.sleep(settings.DELAY)
    data = get_data(settings.PATH_TO_DATA)
    return DataResponse(result=data)
