import os
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Carregar variáveis do .env
load_dotenv()

# Configurações do túnel SSH
SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT", 22))
SSH_USER = os.getenv("SSH_USER")
SSH_KEY = os.path.expanduser(os.getenv("SSH_KEY"))

# Configurações do banco (RDS dentro da VPC)
RDS_HOST = os.getenv("RDS_HOST")
RDS_PORT = int(os.getenv("RDS_PORT", 5432))
RDS_USER = os.getenv("RDS_USER")
RDS_PASS = os.getenv("RDS_PASS")
RDS_DB = os.getenv("RDS_DB")
RDS_SCHEMA = os.getenv("RDS_SCHEMA")

# Criar túnel SSH
def create_tunnel():
    tunnel = SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_pkey=SSH_KEY,
        remote_bind_address=(RDS_HOST, RDS_PORT),
        local_bind_address=("localhost", 5432)
    )
    tunnel.start()
    print("✅ Túnel SSH conectado!")
    return tunnel

# Criar conexão com SQLAlchemy
def get_db_session(tunnel):
    """Cria uma sessão SQLAlchemy conectada ao banco via túnel SSH."""
    db_url = f"postgresql://{RDS_USER}:{RDS_PASS}@localhost:5432/{RDS_DB}"
    engine = create_engine(db_url, connect_args={"options": f"-c search_path={RDS_SCHEMA}"})
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine


def close_connection(session, engine, tunnel):
    """Fecha cursor, conexão e túnel SSH de forma segura."""
    if session:
        session.close()
    if engine:
        engine.dispose()
    if tunnel:
        tunnel.stop()
    print("🔒 Conexão e túnel SSH fechados.")
