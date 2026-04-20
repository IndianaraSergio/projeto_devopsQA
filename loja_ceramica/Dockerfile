# imagem base para o ambiente de testes dasceramica
FROM python:3.9-slim


WORKDIR /app


RUN pip install pytest


COPY . .

# manda rodar os teste assim que a caixa ligar
CMD ["pytest"]