FROM python:3.9-slim

WORKDIR /app

# Instala as dependências do sistema e do Python
RUN apt-get update && apt-get install -y \
    python3-matplotlib \
    && pip install --no-cache-dir matplotlib \
    && rm -rf /var/lib/apt/lists/*

COPY app/ /app/

CMD ["python", "./cifra_monoalfabetica.py"]