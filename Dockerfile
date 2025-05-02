# Imagem base com Python
FROM python:3.12-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para dentro do contêiner
COPY . /app

# Atualiza o pip e instala dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Porta exposta (ajuste se necessário)
EXPOSE 8443

# Comando padrão para iniciar o bot
CMD ["python", "main.py"]
