from fastapi import FastAPI
from services import cep, clima, moeda

app = FastAPI(title="API de Dados Úteis", version="1.0")

@app.get("/cep/{cep_param}")
def consultar_cep(cep_param: str):
    return cep.buscar_cep(cep_param)

@app.get("/clima")
def consultar_clima(lat: float, lon: float):
    return clima.buscar_clima(lat, lon)

@app.get("/moeda/{par}")
def consultar_moeda(par: str = "USD-BRL"):
    return moeda.buscar_moeda(par)