from flask import Flask
import os
import psycopg

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "4628")

@app.route("/")
def inicio():
    try:
        with psycopg.connect(
            host=DB_HOST,
            port=DB_PORT,
            user="postgres",
            password=DB_PASSWORD,
            dbname="postgres"
        ) as conn:
            return "Hola desde Docker! Base de datos conectada."
    except Exception as e:
        return f"App funcionando, pero la BD no conecta: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)