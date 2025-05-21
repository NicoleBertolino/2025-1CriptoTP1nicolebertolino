import sys
import math
from collections import defaultdict

def converter_chave(chave_str):
    """Converte a chave alfabética em numérica"""
    chars_com_indices = [(char, idx) for idx, char in enumerate(chave_str)]
    chars_ordenados = sorted(chars_com_indices, key=lambda x: x[0])
    
    ordem = [0] * len(chave_str)
    for nova_pos, (char, pos_original) in enumerate(chars_ordenados):
        ordem[pos_original] = nova_pos + 1
    
    return ordem

def cifrar_transposicao(texto, chave_num):
    """Aplica a cifra de transposição por colunas"""
    texto_limpo = texto.replace('\n', '').replace(' ', '')
    num_colunas = len(chave_num)
    num_linhas = math.ceil(len(texto_limpo) / num_colunas)
    
    matriz = []
    for i in range(num_linhas):
        inicio = i * num_colunas
        fim = inicio + num_colunas
        linha = list(texto_limpo[inicio:fim].ljust(num_colunas, ' '))
        matriz.append(linha)
    
    ordem_colunas = [i[0] for i in sorted(enumerate(chave_num), key=lambda x:x[1])]
    
    texto_cifrado = []
    for linha in matriz:
        for col in ordem_colunas:
            texto_cifrado.append(linha[col])
    
    return ''.join(texto_cifrado)

def demonstrar_permutacoes(chave_str):
    """Demonstra como diferentes permutações afetam a cifra"""
    print("\nDemonstração de permutações:")
    print(f"Chave original: {chave_str}")
    
    ordem = converter_chave(chave_str)
    print(f"Ordem numérica: {ordem}")
    
    exemplos = [
        sorted(chave_str),
        sorted(chave_str, reverse=True),
        chave_str[::-1],
    ]
    
    for exemplo in exemplos:
        ordem_exemplo = converter_chave(exemplo)
        print(f"\nPermutação: {exemplo} → Ordem: {ordem_exemplo}")  # Linha corrigida

def main():
    if len(sys.argv) < 3:
        print("Uso: python transposicao.py <arquivo_chave> <arquivo_texto>")
        return
    
    arquivo_chave = sys.argv[1]
    arquivo_texto = sys.argv[2]
    
    try:
        with open(arquivo_chave, 'r') as f:
            chave_str = f.read().strip()
        
        with open(arquivo_texto, 'r', encoding='utf-8') as f:
            texto = f.read()
        
        chave_num = converter_chave(chave_str)
        texto_cifrado = cifrar_transposicao(texto, chave_num)
        
        with open('transposicaoCifrado.txt', 'w', encoding='utf-8') as f:
            f.write(texto_cifrado)
        
        print(f"Texto cifrado salvo em 'transposicaoCifrado.txt'")
        print(f"Chave usada: {chave_str} → {chave_num}")
        
        demonstrar_permutacoes(chave_str)
    
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()