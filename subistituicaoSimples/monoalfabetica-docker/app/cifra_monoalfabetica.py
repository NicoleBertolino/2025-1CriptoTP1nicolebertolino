import random
import string
from collections import Counter
import matplotlib.pyplot as plt

def gerar_chave_aleatoria():
    """Gera uma permutação aleatória do alfabeto como chave"""
    alfabeto = list(string.ascii_lowercase)
    random.shuffle(alfabeto)
    return ''.join(alfabeto)

def cifrar_monoalfabetica(texto, chave):
    """Aplica a cifra monoalfabética"""
    mapeamento = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        chave.lower() + chave.upper()
    )
    return texto.translate(mapeamento)

def analise_frequencia(texto_cifrado):
    """Realiza análise de frequência do texto cifrado"""
    # Filtra apenas letras e conta frequências
    letras = [c.lower() for c in texto_cifrado if c.isalpha()]
    contador = Counter(letras)
    
    # Frequências do português (ordem aproximada)
    freq_portugues = {
        'a': 14.63, 'e': 12.57, 'o': 10.73, 's': 7.81, 'r': 6.53,
        'i': 6.18, 'n': 5.05, 'd': 4.99, 'm': 4.74, 'u': 4.63,
        't': 4.34, 'c': 3.88, 'l': 2.78, 'p': 2.52, 'v': 1.67,
        'g': 1.30, 'h': 1.28, 'q': 1.20, 'b': 1.04, 'f': 1.02,
        'z': 0.46, 'j': 0.40, 'x': 0.21, 'k': 0.02, 'w': 0.01,
        'y': 0.01
    }
    
    # Ordena por frequência
    letras_cifradas = [item[0] for item in contador.most_common()]
    letras_portugues = [item[0] for item in sorted(freq_portugues.items(), key=lambda x: x[1], reverse=True)]
    
    # Sugere mapeamento
    sugestao = dict(zip(letras_cifradas, letras_portugues))
    
    # Gera histograma
    plt.figure(figsize=(12, 6))
    plt.bar(contador.keys(), contador.values())
    plt.title('Frequência de Letras no Texto Cifrado')
    plt.savefig('frequencia.png')
    plt.close()
    
    return contador, sugestao

def main():
    # 1. Gerar chave aleatória
    chave = gerar_chave_aleatoria()
    with open('CHAVE.txt', 'w') as f:
        f.write(chave)  # CORREÇÃO: estava 'chueve' em vez de 'chave'
    
    # 2. Ler texto claro
    with open('CLARO.txt', 'r', encoding='utf-8') as f:
        texto_claro = f.read()
    
    # 3. Cifrar texto
    texto_cifrado = cifrar_monoalfabetica(texto_claro, chave)
    with open('claroEmono.txt', 'w', encoding='utf-8') as f:
        f.write(texto_cifrado)
    
    # 4. Análise de frequência
    contador, sugestao = analise_frequencia(texto_cifrado)
    
    print("Análise de Frequência Completa!")
    print("\nTop 10 letras mais frequentes:")
    for letra, freq in contador.most_common(10):
        print(f"{letra}: {freq} ocorrências")
    
    print("\nSugestão de mapeamento (cifrado → provável original):")
    for cif, orig in sugestao.items():
        print(f"{cif} → {orig}")
    
    print("\nHistograma de frequências salvo em 'frequencia.png'")

if __name__ == "__main__":
    main()