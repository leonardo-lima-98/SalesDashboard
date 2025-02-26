from sqlalchemy import text 
from db_connection import create_tunnel, get_db_session, close_connection

# Criar túnel SSH e sessão do banco
tunnel = create_tunnel()
session, engine = get_db_session(tunnel)

result = session.execute(text("SELECT NOW();")) 

# Exibir o resultado
now = result.fetchone()
print("Conexão com PostgreSQL bem-sucedida:", now[0])

# Fechar tudo com a nova função
close_connection(session, engine, tunnel)