import hashlib

# Função para gerar hash SHA-256
def gerar_hash(arquivo):
    with open(arquivo, 'rb') as f:
        bytes = f.read()
        hash = hashlib.sha256(bytes).hexdigest()
        return hash

# Função da Cifra de César
def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Mantém o caso (maiúsculo/minúsculo)
            offset = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - offset + deslocamento) % 26 + offset)
        else:
            resultado += char
    return resultado

# Função para quebra por força bruta
def quebra_forca_bruta(texto_cifrado):
    print("\nQuebra por força bruta:")
    for k in range(1, 26):
        decifrado = cifra_cesar(texto_cifrado, -k)
        print(f"Deslocamento {k}: {decifrado[:50]}...")  # Mostra apenas os primeiros 50 caracteres

# 1. Gerar hash do arquivo claro
hash_claro = gerar_hash('CLARO.txt')
with open('CLAROsigSHA256.txt', 'w') as f:
    f.write(hash_claro)

# 2. Ler o arquivo claro
with open('CLARO.txt', 'r', encoding='utf-8') as f:
    texto_claro = f.read()

# 3. Solicitar deslocamento ao usuário
try:
    k = int(input("Digite o valor de deslocamento (k) para a Cifra de César: "))
except ValueError:
    print("Valor inválido. Usando k=3 como padrão.")
    k = 3

# 4. Aplicar Cifra de César
texto_cifrado = cifra_cesar(texto_claro, k)
with open('claroEcesar.txt', 'w', encoding='utf-8') as f:
    f.write(texto_cifrado)

# 5. Realizar quebra por força bruta
quebra_forca_bruta(texto_cifrado)

print("\nOperação concluída. Arquivos gerados:")
print("- CLAROsigSHA256.txt (hash SHA-256 do texto claro)")
print("- claroEcesar.txt (texto cifrado com César)")