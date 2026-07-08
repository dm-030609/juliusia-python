from julius.sanitizador import SanitizadorBR

def test_sanitizar_valor_remove_formatacao_brl():
    entrada = "1.250,90"

    resultado = SanitizadorBR.sanitizar_valor(entrada)

    assert resultado == 1250.90



def test_formatar_brl_adiciona_simbolo_e_pontuacao():
    entrada = 1250.90

    resultado = SanitizadorBR.formatar_brl(entrada)

    assert resultado == "R$ 1.250,90"