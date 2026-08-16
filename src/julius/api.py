from fastapi import FastAPI
from julius.gasto import Gasto
from julius.registro import RegistroFinanceiro
from julius.relatorio import RelatorioFinanceiro
from julius.sanitizador import SanitizadorBR
from pydantic import BaseModel

app = FastAPI()
registro = RegistroFinanceiro()
relatorio = RelatorioFinanceiro(registro)

class GastoInput(BaseModel):
    descricao: str
    valor: str
    categoria: str
    data: str


@app.post("/gastos")
def criar_gasto(entrada: GastoInput):
    valor_limpo = SanitizadorBR.sanitizar_valor(entrada.valor)
    gasto = Gasto(data = entrada.data, categoria = entrada.categoria, valor = valor_limpo, descricao = entrada.descricao)
    registro.adicionar(gasto)

    return {"mensagem": "Gasto adicionado", "total": registro.total()}


@app.get("/gastos")
def listar_gastos():
    return {"gastos": [str(g) for g in  registro.todos()], "total": registro.total()}

@app.get("/relatorio/categorias")
def relatorio_categorias():
    return {"gastos": relatorio.gerar_por_categoria()}

@app.get("/relatorio/mensal/{mes}/{ano}")
def relatorio_mensal(mes: str, ano: str):
    return {"gastos": relatorio.resumo_mensal(f"{mes}/{ano}")}