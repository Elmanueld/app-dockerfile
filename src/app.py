from flask import Flask
import os
import time
import pymysql

app = Flask(__name__)


def database_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "appdb"),
        connect_timeout=3,
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.get("/")
def hello():
    last_error = None
    for attempt in range(10):
        try:
            with database_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("CREATE TABLE IF NOT EXISTS visits (id INT AUTO_INCREMENT PRIMARY KEY, visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
                    cursor.execute("INSERT INTO visits () VALUES ()")
                    cursor.execute("SELECT COUNT(*) AS total FROM visits")
                    total = cursor.fetchone()["total"]
            return f"<h1>¡Hola mundo!</h1><p>Conectado a MySQL correctamente.</p><p>Visitas registradas: {total}</p>"
        except pymysql.MySQLError as error:
            last_error = error
            time.sleep(2)
    return f"No se pudo conectar a MySQL: {last_error}", 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
