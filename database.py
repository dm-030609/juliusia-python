import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

# 2. Pega a URL que você colocou lá (se não achar, dá erro)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não foi encontrada no .env")

# 3. Cria o "Motor" que vai conversar com a Neon
engine = create_engine(DATABASE_URL)

# 4. Função que cria as tabelas no banco se elas não existirem
def criar_tabelas():
    SQLModel.metadata.create_all(engine)

# 5. Função que abre uma "Sessão" (conexão) toda vez que a API precisar
def get_session():
    with Session(engine) as session:
        yield session
