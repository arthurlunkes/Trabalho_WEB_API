# Use a imagem oficial do Python
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o contêiner
COPY . .

# Exponha a porta em que o aplicativo FastAPI será executado
EXPOSE 8000

# Comando para iniciar o aplicativo FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
