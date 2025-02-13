import psycopg2
from psycopg2 import pool

class Database:
    """Gerenciador de conexão com PostgreSQL usando connection pooling."""

    def __init__(self):
        """Inicializa o pool de conexões."""
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="dizimei",
            user="gustavo",
            password="IlK5qZ54429Q",
            host="dizimei-dev.cbeoqj4emryb.us-east-1.rds.amazonaws.com",
            port=5432,
        )

    def get_connection(self):
        """Obtém uma conexão do pool."""
        return self.connection_pool.getconn()

    def release_connection(self, connection):
        """Devolve a conexão para o pool."""
        self.connection_pool.putconn(connection)

    def close_all_connections(self):
        """Fecha todas as conexões do pool."""
        self.connection_pool.closeall()