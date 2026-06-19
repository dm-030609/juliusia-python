from julius.gasto import Gasto

class RegistroFinanceiro:
    def __init__(self):
        self._gastos = []

    def todos(self) -> list:
        return self._gastos 


    def adicionar(self, gasto):
        self._gastos.append(gasto)

    def total(self) -> float:
        return sum(gasto.valor for gasto in self._gastos)

    def filtrar_por_categoria(self, categoria: str) -> list:
        resultado = []
        # for gasto in self._gastos:
        #     if gasto.categoria == categoria:
        #         resultado.append(gasto)
        #
        # return resultado

        #comprehensions - modo pythonico de escrita
        return [g for g in self._gastos if g.categoria == categoria ]


    def filtrar_por_data(self, data: str) -> list:
        resultado = []
        # for gasto in self._gastos:
        #     if gasto.data == data:
        #         resultado.append(gasto)
        # return resultado

        return [g for g in self._gastos if g.data == data]


    def __len__(self):
        return len(self._gastos)


    def resumo(self) -> str:
        if not self._gastos:
            return "Nenhum gasto encontrado"

        linhas = [str(gasto) for gasto in self._gastos]
        linhas.append(f"Total: R${self.total():.2f}")

        return "\n".join(linhas)

    def __str__(self) -> str:
        return f"total= {self.total():.2f}, gastos(qtd)= {len(self)}"