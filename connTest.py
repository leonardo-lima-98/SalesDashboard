import psycopg2
import os
from sshtunnel import SSHTunnelForwarder
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Configurações do túnel SSH
SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = int(os.getenv("SSH_PORT", 22))  # Porta padrão 22
SSH_USER = os.getenv("SSH_USER")
SSH_KEY = os.getenv("SSH_KEY")

# Configurações do banco (RDS dentro da VPC)
RDS_HOST = os.getenv("RDS_HOST")
RDS_PORT = int(os.getenv("RDS_PORT", 5432))
RDS_USER = os.getenv("RDS_USER")
RDS_PASS = os.getenv("RDS_PASS")
RDS_DB = os.getenv("RDS_DB")
RDS_SCHEMA = os.getenv("RDS_SCHEMA")

# Criar túnel SSH
with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_KEY,
    remote_bind_address=(RDS_HOST, RDS_PORT),
    local_bind_address=("localhost", 5432)
) as tunnel:
    
    print("Túnel SSH conectado!")

    # Conectar no PostgreSQL via túnel
    conn = psycopg2.connect(
        dbname=RDS_DB,
        user=RDS_USER,
        password=RDS_PASS,
        host="localhost",  # Conecta no túnel
        port=5432,  # Mesma porta do túnel
        options=f"-c search_path={RDS_SCHEMA}"  # Define o schema
    )
    
    cur = conn.cursor()
    cur.execute("SELECT NOW();")  # Apenas para testar
    print("Conexão com PostgreSQL bem-sucedida:", cur.fetchone())

    cur.close()
    conn.close()
    print("Conexão fechada.")
