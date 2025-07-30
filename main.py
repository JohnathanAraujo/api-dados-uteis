from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from services import cep, clima, moeda

app = FastAPI(title="API de Dados Úteis", version="1.0")

# Configurar CORS para permitir comunicação com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "API de Dados Úteis - Acesse /static/index.html para a interface"}

@app.get("/cep/{cep_param}")
def consultar_cep(cep_param: str):
    return cep.buscar_cep(cep_param)

@app.get("/clima")
def consultar_clima(lat: float, lon: float):
    return clima.buscar_clima(lat, lon)

@app.get("/moeda/{par}")
def consultar_moeda(par: str = "USD-BRL"):
    return moeda.buscar_moeda(par)