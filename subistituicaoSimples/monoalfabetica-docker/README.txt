Comandos para executar local:

comando docker para criar a imagem cifra de cesar
docker build -t monoalphabetic-crypto .

comando para executar imagem via docker:
docker run -it --rm -v "$(pwd)/app:/app" monoalphabetic-crypto
 

Comandos para enviar imagens para o docker hub
1. Renomear sua imagem local para o padrão Docker Hub
docker tag monoalphabetic-crypto nicolebertolino/2025-1criptotp1nicolebertolino:monoalphabetic

2. Fazer login no Docker Hub via terminal
docker login

3. Enviar a imagem para o Docker Hub
docker push nicolebertolino/2025-1criptotp1nicolebertolino:monoalphabetic
							
							
							
Como outros usarão a minha imagem do docker hub:
docker pull nicolebertolino/2025-1criptotp1nicolebertolino:monoalphabetic

E executar com:
docker run -it --rm nicolebertolino/2025-1criptotp1nicolebertolino:monoalphabetic



