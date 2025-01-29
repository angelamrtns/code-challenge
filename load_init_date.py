import psycopg2
import os

def load_sql_file(sql_file_path, conn_params):
    """
    Lê o arquivo .sql e executa no banco informado.
    :param sql_file_path: Caminho completo do arquivo SQL.
    :param conn_params: Dicionário com parâmetros de conexão do psycopg2.
    """
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Conecta no Postgres
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_script)
        conn.commit()
    print(f"Arquivo {sql_file_path} executado com sucesso.")

if __name__ == "__main__":
    # Parâmetros de conexão com o banco Northwind (ajuste se necessário)
    conn_params = {
        "host": "localhost",
        "port": 5432,
        "dbname": "northwind",
        "user": "northwind_user",
        "password": "thewindisblowing"
    }

    # Caminho do arquivo .sql, por exemplo: ./data/northwind.sql
    sql_path = os.path.join("data", "northwind.sql")
    

    load_sql_file(sql_path, conn_params)
