# Hello World Docker + Kubernetes + CI/CD

Este projeto é uma aplicação simples que retorna "Hello World" em um endpoint, utilizando Flask, Docker, Minikube e GitHub Actions para CI/CD.

## Passos

1. Criação de uma imagem Docker multistaging.
2. Publicação da imagem no Docker Hub.
3. Deploy da aplicação em um cluster Minikube.
4. Configuração de pipeline CI/CD para build e push da imagem para o Docker Hub.

### Tecnologias usadas

- Python
- Flask
- Docker
- Kubernetes (Minikube)
- GitHub Actions

## Como rodar localmente

### Opção 1: Build da imagem localmente

1. Clone o repositório.
2. Execute `docker build -t hello-world .`
3. Execute `docker run -p 5000:5000 hello-world`
4. Acesse `http://localhost:5000`

### Opção 2: Baixar a imagem diretamente do Docker Hub

1. Execute `docker pull isabe1ltenorio/hello-world`
2. Execute `docker run -p 5000:5000 isabe1ltenorio/hello-world`
3. Acesse `http://localhost:5000`

## CI/CD com GitHub Actions

Ao fazer push para o branch `main`, a pipeline faz build e push da imagem Docker automaticamente para o Docker Hub.
