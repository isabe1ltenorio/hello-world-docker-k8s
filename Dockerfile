# Etapa 1: Construir a aplicação
FROM python:3.11-slim AS builder

WORKDIR /app

# Copiar os arquivos de requisitos e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Criar a imagem final
FROM python:3.11-slim

WORKDIR /app

# Copiar os arquivos da etapa de construção
COPY --from=builder /app /app

# Copiar a aplicação
COPY app.py .

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para executar a aplicação
CMD ["python", "app.py"]


