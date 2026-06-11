# JuliusIA — Python

Agente financeiro pessoal com IA. Permite registrar, consultar e analisar gastos via chat (Telegram/WhatsApp).

Esta é a versão Python — reescrita orientada a objetos a partir do protótipo funcional em n8n + JavaScript.

## Estrutura

```
src/julius/
├── gasto.py          # Modelo de um lançamento financeiro
├── registro.py       # Repositório em memória (coleção de gastos)
├── sanitizador.py    # Conversão de formato BR ↔ float
└── relatorio.py      # Geração de relatórios e resumos
```

## Stack

- Python 3.12+
- uv (gerenciamento de dependências)
- ruff (linting)
- pytest (testes)
