Comandos para executar local:

Comandos para Execução

comando docker para criar a imagem cifra vernam:
docker build -t vernam-crypto .

comando para executar imagem via docker:
docker run -it --rm -v "$(pwd)/app:/app" vernam-crypto CHAVE.txt
 

Comandos para enviar imagens para o docker hub
1. Renomear sua imagem local para o padrão Docker Hub
docker tag cesar-crypto nicolebertolino/2025-1criptotp1nicolebertolino:vernam

2. Fazer login no Docker Hub via terminal
docker login

3. Enviar a imagem para o Docker Hub
docker push nicolebertolino/2025-1criptotp1nicolebertolino:vernam
							
							
							
Como outros usarão a minha imagem do docker hub:
docker pull nicolebertolino/2025-1criptotp1nicolebertolino:vernam

E executar com:
docker run -it --rm nicolebertolino/2025-1criptotp1nicolebertolino:vernam


RESPOSTAS:

## Explicação dos Arquivos Gerados
*VernamRAW.txt:
      Contém o resultado bruto do XOR tentando ser interpretado como texto UTF-8
      Geralmente ilegível porque o XOR altera os bytes de forma que não correspondem mais a caracteres UTF-8 válidos
      Usamos errors='replace' para substituir bytes inválidos por um caractere de substituição (�)

*VernamBin.txt:
       Contém os bytes exatos resultantes da operação XOR
       Arquivo binário puro, sem tentativa de interpretação como texto
       Preserva exatamente o resultado da cifra sem modificações

*VernamUtf8.txt:
      Tenta decodificar o resultado de volta para UTF-8
       Na maioria dos casos falha, demonstrando como a cifragem corrompe a estrutura UTF-8
       Se por acaso funcionar, mostra que a cifragem foi reversível sem perdas

*VernamBase64.txt:
        Representação segura e legível do resultado binário
        Codificação Base64 permite visualizar o resultado em formato texto ASCII
     Necessário para transmissão segura do texto cifrado por canais que exigem texto

##Diferença entre Vernam e One-Time Pad (OTP)
*Cifra de Vernam:
       Usa XOR entre texto e chave
       Permite repetição da chave se for menor que o texto
      Não é inquebrável matematicamente quando a chave é repetida
      Vulnerável a ataques quando a mesma chave é usada múltiplas vezes

*One-Time Pad (OTP):
       Também usa XOR entre texto e chave
       Exige que a chave tenha exatamente o mesmo tamanho do texto
       Nunca reutiliza a chave (daí "one-time")

*É inquebrável matematicamente quando:
   A chave é verdadeiramente aleatória
   Nunca é reusada
   Mantida em segredo
   Tão longa quanto a mensagem

##Por que UTF-8 + XOR não é suficiente?
*UTF-8 tem estrutura complexa:
    Caracteres podem usar 1-4 bytes
    XOR pode corromper essa estrutura
    Pode criar sequências inválidas de bytes UTF-8

*Problemas de visualização:
      Muitos bytes resultantes não correspondem a caracteres imprimíveis
      Podem ser interpretados como caracteres de controle

*Necessidade de codificação:
     Para armazenar/transmitir o resultado de forma segura
     Base64 garante que todos os caracteres são ASCII imprimíveis
    Permite reconstrução exata dos bytes originais