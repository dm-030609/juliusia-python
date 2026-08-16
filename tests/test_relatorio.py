from julius.gasto import Gasto
from julius.registro import RegistroFinanceiro
from julius.relatorio import RelatorioFinanceiro


def test_relatorio_por_categoria():
 registro = RegistroFinanceiro()

 g1 = Gasto(data = "11/07", categoria = "Alimentação", valor = 30.0, descricao = "cafe da manha")
 g2 = Gasto(data = "10/07", categoria = "Alimentação", valor =  50.0, descricao = "cafe da tarde")
 g3 = Gasto(data = "09/07", categoria = "Transporte", valor =15.0, descricao = "gasolina")
 registro.adicionar(g1)
 registro.adicionar(g2)
 registro.adicionar(g3)

 relatorio = RelatorioFinanceiro(registro)

 resultado = relatorio.gerar_por_categoria()

 assert resultado["Alimentação"] == 80.0
 assert resultado["Transporte"] == 15.0
 assert len(resultado) == 2 