import json
import random

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


alertsMiddle = FastAPI()

class JsonModelObj(BaseModel):
    status: str
    labels: dict
    annotations: dict

class InheritJsonModel(BaseModel):
    alerts: List[JsonModelObj]

def gen_path() -> str:
    """Funçao para acrescentar um numero ao nome do arquivo escolhido.
    Devido ao nivel de cansaço, ainda nao pensei numa soluçao mais adequada.
    Contudo, pretendo implementar um banco de dados para armazenar as POST REQUESTS"""

    return f"./dump_data/dumped_alerts{random.randint(1, 1000000)}.json"


@alertsMiddle.post("/alerts")
def read_alerts(file: InheritJsonModel):
    with open(gen_path(), "+a") as alerts_json:
        alerts_json.write(json.dumps(file.model_dump(), indent=2))
    return {"msg": "successfully received alert!"}
