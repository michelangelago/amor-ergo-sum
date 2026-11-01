FROM python:3.15-slim

WORKDIR /app

COPY . .
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

CMD ["python", "main.py"]