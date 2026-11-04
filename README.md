# Hola mundo con Docker Compose y MySQL

Aplicación web sencilla en Python (Flask) conectada a MySQL. Cada visita crea un registro en la base de datos.

## Requisitos
- Docker Desktop con Docker Compose

## Ejecutar
Desde la carpeta del proyecto:

```bash
docker compose up --build
```

Abre http://localhost:5000. Para detener los servicios usa `Ctrl+C` y luego `docker compose down`. Para borrar también los datos guardados, ejecuta `docker compose down -v`.

La app Flask está en `src/app.py`; Dockerfile y dependencias están en `src/`. Compose inicia la aplicación y MySQL, y espera a que MySQL esté listo antes de iniciar la app.
