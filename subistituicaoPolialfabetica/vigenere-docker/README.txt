Comando para Encriptação:
python vigenere.py cifrar CLARO.txt claroEvigenere.txt nicolebe

Comando para Decriptação:
python vigenere.py decifrar claroEvigenere.txt decifrado.txt nicolebe

Comando para Análise de Kasiski:
python vigenere.py kasiski claroEvigenere.txt analise_kasiski.txt


Comandos para executar local:

comando docker para criar a imagem cifra vigenère
docker build -t vigenere-crypto .

Comando docker para executar a cifragem (encriptação): 
docker run -it --rm -v "$(pwd)/app:/app" vigenere-crypto cifrar CLARO.txt claroEvigenere.txt nicolebe
 
Comando para executar a decifragem (decriptação):
docker run -it --rm -v "$(pwd)/app:/app" vigenere-crypto decifrar claroEvigenere.txt decifrado.txt nicolebe

Comando para executar a análise de Kasiski: 
docker run -it --rm -v "$(pwd)/app:/app" vigenere-crypto kasiski claroEvigenere.txt analise_kasiski.txt


Comandos para enviar imagens para o docker hub
1. Renomear sua imagem local para o padrão Docker Hub
docker tag vigenere-crypto nicolebertolino/2025-1criptotp1nicolebertolino:vigenere

2. Fazer login no Docker Hub via terminal
docker login

3. Enviar a imagem para o Docker Hub
docker push nicolebertolino/2025-1criptotp1nicolebertolino:vigenere
							
							
							
Como outros usarão a minha imagem do docker hub:
docker pull nicolebertolino/2025-1criptotp1nicolebertolino:vigenere

E executar com:
docker run -it --rm nicolebertolino/2025-1criptotp1nicolebertolino:vigenere



