from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import iniciar_banco
from contextlib import asynccontextmanager
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'bulex.db')

@asynccontextmanager
async def lifespan(app: FastAPI):
    iniciar_banco()
    yield

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

def busca_medicamento(id_med):
    with sqlite3.connect(DB_PATH) as conn:  # <-- caminho absoluto
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicamentos WHERE id = ?", (id_med,))
        return cursor.fetchone()

@app.get("/", response_class=HTMLResponse)
async def tela_inicial(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/medicamento/{id}", response_class=HTMLResponse)
async def ler_bula(request: Request, id: int):
    medicamento = busca_medicamento(id)

    if not medicamento:
        return HTMLResponse(content="<h1>Medicamento não encontrado</h1>", status_code=404)

    return templates.TemplateResponse(
        request=request,
        name="bula.html",
        context={"med": medicamento}
    )