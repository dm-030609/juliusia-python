from julius.gasto import Gasto

class RegistroFinanceiro:
    def __init__(self):
        self._gastos = []


    def adicionar(self, gasto):
        self._gastos.append(gasto)

    def total(self) -> float:
        return sum(gasto.valor for gasto in self._gastos)

    def filtrar_por_categoria(self, categoria: str) -> list:
        resultado = []
        for gasto in self._gastos:
            if gasto.categoria == categoria:
                resultado.append(gasto)

        return resultado


    def filtrar_por_data(self, data: str) -> list:
        resultado = []
        for gasto in self._gastos:
            if gasto.data == data:
                resultado.append(gasto)
        return resultado


    def __len__(self):
        return len(self._gastos)
