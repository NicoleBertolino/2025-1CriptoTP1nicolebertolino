Comandos para executar local:

comando docker para criar a imagem:
docker build -t transposicao-crypto .

comando para executar imagem via docker:
docker run -it --rm -v "$(pwd)/app:/app" transposicao-crypto CHAVE.txt CLARO.txt
 

Comandos para enviar imagens para o docker hub
1. Renomear sua imagem local para o padrão Docker Hub
docker tag cesar-crypto nicolebertolino/2025-1criptotp1nicolebertolino:transposicao

2. Fazer login no Docker Hub via terminal
docker login

3. Enviar a imagem para o Docker Hub
docker push nicolebertolino/2025-1criptotp1nicolebertolino:transposicao
							
							
							
Como outros usarão a minha imagem do docker hub:
docker pull nicolebertolino/2025-1criptotp1nicolebertolino:transposicao

E executar com:
docker run -it --rm nicolebertolino/2025-1criptotp1nicolebertolino:transposicao



Explicação do Funcionamento
1. Conversão da Chave Alfabética para Numérica
A função converter_chave:
Recebe uma string (ex: "nicolebe")
Para cada caractere, armazena sua posição original
Ordena os caracteres alfabeticamente
Atribui números de ordem baseado na posição original
Exemplo com "nicolebe":
 
 
Copy
 
Download
Plain Text
Posições originais: n(0), i(1), c(2), o(3), l(4), e(5), b(6), e(7)
Ordenado: b, c, e, e, i, l, n, o
Ordem numérica: [6, 3, 2, 7, 5, 4, 1, 8] 