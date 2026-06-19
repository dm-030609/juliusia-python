# Imagem base: Python 3.12 enxuto (bate com requires-python ">=3.12" do pyproject).
# "-slim" = versão pequena, sem ferramentas extras → imagem mais leve e segura.
FROM python:3.12-slim

# Traz o binário do uv direto da imagem oficial deles, sem instalar via pip.
# É o jeito recomendado e mais rápido: copia só o executável pronto.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Pasta de trabalho dentro do container. Tudo daqui pra frente acontece em /app.
WORKDIR /app

# --- Truque de cache: copiar manifestos ANTES do código ---
# Docker constrói em camadas e reaproveita as que não mudaram.
# Enquanto pyproject.toml/uv.lock forem iguais, ele pula o passo lento de
# baixar dependências em builds futuros. Só recompila deps se elas mudarem.
COPY pyproject.toml uv.lock ./

# Instala SÓ as dependências (sem o projeto ainda), exatamente como travadas
# no uv.lock (--frozen = não recalcula versões), sem deps de desenvolvimento.
RUN uv sync --frozen --no-install-project --no-dev

# Agora sim o código-fonte entra (esta camada muda toda hora; por isso vem depois).
COPY . .

# Instala o próprio projeto → resolve o pacote `julius` do layout src/.
RUN uv sync --frozen --no-dev

# O Render injeta a porta real na variável $PORT em tempo de execução.
# 8000 é só o default pra rodar local sem o Render.
ENV PORT=8000
EXPOSE 8000

# Comando que sobe a API quando o container liga.
# - "sh -c" → precisamos da shell pra expandir ${PORT}.
# - python -m uvicorn → o jeito blindado que você aprendeu (interpretador certo).
# - --host 0.0.0.0 → OBRIGATÓRIO em container. Sem isso ele só escuta "localhost"
#   de dentro do container e ninguém de fora consegue acessar.
CMD ["sh", "-c", "uv run python -m uvicorn julius.api:app --host 0.0.0.0 --port ${PORT}"]
