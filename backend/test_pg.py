import psycopg

conn = psycopg.connect(
    dbname="prestamos_universitarios_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5433",  # cambia a 5432 si tu servidor usa ese puerto
)

print("Conexión OK")
conn.close()
