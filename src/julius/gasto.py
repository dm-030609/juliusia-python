class Gasto:
    def __init__(self, data: str, categoria: str, valor: float, descricao: str):
        self.data = data
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao


    def __str__(self):
        return f"{self.data} | {self.categoria} | R${self.valor:.2f} | {self.descricao}"


    def __repr__(self):
        return f"Gasto(data='{self.data}', valor={self.valor})"

