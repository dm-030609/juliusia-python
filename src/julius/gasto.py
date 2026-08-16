from typing import Optional
from sqlmodel import SQLModel, Field


# O "table=True" diz ao SQLModel para criar a tabela no banco
class Gasto(SQLModel, table=True):
    # Field(primary_key=True) cria a coluna ID, e o banco gera o número sozinho (por isso o Optional/None).
    id: Optional[int] = Field(default=None, primary_key=True)

    # As variáveis viram as colunas da sua tabela usando Type Hints do Python
    data: str
    categoria: str
    valor: float
    descricao: str

    def __str__(self):
        return f"{self.data} | {self.categoria} | R${self.valor:.2f} | {self.descricao}"

    # O SQLModel já cuida do __repr__ por você, então deletamos a função antiga!
