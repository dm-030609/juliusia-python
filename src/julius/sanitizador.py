class SanitizadorBR:
    @staticmethod
    def sanitizar_valor(valor_str: str) -> float:
        valor_str = valor_str.replace("R$", "")
        valor_str = valor_str.strip()
        valor_str = valor_str.replace(".", "")
        valor_str = valor_str.replace(",", ".")

        return float(valor_str)



    @staticmethod
    def formatar_brl(valor_str: float) -> str:
        valor_str = f"{valor_str:,.2f}"
        valor_str = valor_str.replace(".", "@")
        valor_str = valor_str.replace(",", ".")
        valor_str = valor_str.replace("@", ",")

        return f"R$ {valor_str}"

