import os
from ssh import SSHForwarder
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fast_zero.models import Base

# Carregar variáveis do .env
load_dotenv()

# Configurações do banco (RDS dentro da VPC)
RDS_HOST = os.getenv("RDS_HOST")
RDS_PORT = int(os.getenv("RDS_PORT", 5432))
RDS_USER = os.getenv("RDS_USER")
RDS_PASS = os.getenv("RDS_PASS")
RDS_DB = os.getenv("RDS_DB")
RDS_SCHEMA = os.getenv("RDS_SCHEMA")

# Criar conexão com SQLAlchemy
def get_db_session():
    """Cria uma sessão SQLAlchemy conectada ao banco via túnel SSH."""
    db_url = f"postgresql://{RDS_USER}:{RDS_PASS}@localhost:5432/{RDS_DB}"
    engine = create_engine(db_url, connect_args={"options": f"-c search_path={RDS_SCHEMA}"})
    Session = sessionmaker(bind=engine)
    session = Session()
    print("✅ Sessão criada!")
    return session, engine


def open_connection():
    # Criar túnel SSH e sessão do banco
    session, engine = get_db_session()

    Base.metadata.create_all(engine)
    return session, engine


def close_connection(session, engine):
    """Fecha cursor, conexão e túnel SSH de forma segura."""
    if session:
        session.close()
    if engine:
        engine.dispose()
    print("🔒 Conexão fechada.")
