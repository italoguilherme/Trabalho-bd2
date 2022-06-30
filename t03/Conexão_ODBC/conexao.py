import psycopg2

host = 'localhost'
dbname = 'AtividadesBD'
user = 'postgres'
password = 'postgres'
port = '5432'
cone = None
cur = None

def ConexaoBanco():
    try:
        cone =psycopg2.connect(
            host = host,
            dbname = dbname,
            user = user,
            password = password,
            port = port
        )
        return cone

    except Exception as error:
        print(errorcod)
