from datetime import datetime

from julius import registro
from julius.registro import RegistroFinanceiro


class RelatorioFinanceiro:
    def __init__(self, registro: RegistroFinanceiro):
        self._registro = registro

    def gerar_por_categoria(self) -> dict:
        totais = {}
        for gasto in self._registro.todos():
            totais[gasto.categoria] = totais.get(gasto.categoria, 0) + gasto.valor
        return totais


    def total_por_periodo(self, inicio: str, fim: str) -> float:

        data_inicio = datetime.strptime(inicio, "%d/%m/%Y").date()
        data_fim = datetime.strptime(fim, "%d/%m/%Y").date()

        total = 0.0

        for gasto in self._registro.todos():
            gasto_data = datetime.strptime(gasto.data, "%d/%m/%Y").date()
            if data_inicio <= gasto_data <= data_fim:
                total += gasto.valor

        return total

    def resumo_mensal(self, mes: str) -> str:
        gasto_do_mes = [gasto for gasto in self._registro.todos() if gasto.data[3:] == mes]

        if not gasto_do_mes:
            return f"Nenhum gasto em {mes}"

        linhas = [str(gasto) for gasto in gasto_do_mes]
        total = sum(gasto.valor for gasto in gasto_do_mes)
        linhas.append(f"Total: R${total:.2f}")
        return "\n".join(linhas)



