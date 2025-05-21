import sys
import math
from collections import defaultdict, Counter
import re

def processar_texto(texto):
    """Remove caracteres não alfabéticos e converte para maiúsculas"""
    return re.sub(r'[^A-Za-z]', '', texto).upper()

def gerar_chave(texto, chave):
    """Repete a chave para cobrir todo o texto"""
    return (chave * (len(texto) // len(chave) + 1))[:len(texto)]

def cifrar_vigenere(texto, chave, modo='cifrar'):
    """Cifra ou decifra usando Vigenère"""
    texto_proc = processar_texto(texto)
    chave_proc = processar_texto(chave)
    chave_expandida = gerar_chave(texto_proc, chave_proc)
    
    resultado = []
    for i in range(len(texto_proc)):
        if modo == 'cifrar':
            novo_char = chr(((ord(texto_proc[i]) + ord(chave_expandida[i]) - 2 * ord('A')) % 26) + ord('A'))
        else:
            novo_char = chr(((ord(texto_proc[i]) - ord(chave_expandida[i]) + 26) % 26) + ord('A'))
        resultado.append(novo_char)
    
    return ''.join(resultado)

def encontrar_sequencias_repetidas(texto, tamanho_min=3):
    """Encontra sequências repetidas para análise de Kasiski"""
    sequencias = defaultdict(list)
    for i in range(len(texto) - tamanho_min + 1):
        seq = texto[i:i+tamanho_min]
        sequencias[seq].append(i)
    
    return {seq: pos for seq, pos in sequencias.items() if len(pos) > 1}

def calcular_mdc(lista):
    """Calcula o MDC de uma lista de números"""
    def mdc(a, b):
        while b:
            a, b = b, a % b
        return a
    
    current_mdc = lista[0]
    for num in lista[1:]:
        current_mdc = mdc(current_mdc, num)
        if current_mdc == 1:
            return 1
    return current_mdc

def analise_kasiski(texto_cifrado):
    """Realiza análise de Kasiski para estimar tamanho da chave"""
    texto_proc = processar_texto(texto_cifrado)
    sequencias = encontrar_sequencias_repetidas(texto_proc)
    
    distancias = []
    for seq, posicoes in sequencias.items():
        for i in range(len(posicoes) - 1):
            distancias.append(posicoes[i+1] - posicoes[i])
    
    if not distancias:
        return None
    
    # Agrupa os fatores mais comuns
    fatores = []
    for dist in distancias:
        for i in range(2, min(20, dist//2 + 1)):
            if dist % i == 0:
                fatores.append(i)
    
    contador_fatores = Counter(fatores)
    return contador_fatores.most_common(5)

def main():
    if len(sys.argv) < 4:
        print("Uso: python vigenere.py <modo> <arquivo_entrada> <arquivo_saida> [chave]")
        print("Modos: cifrar, decifrar, kasiski")
        return
    
    modo = sys.argv[1]
    arquivo_entrada = sys.argv[2]
    arquivo_saida = sys.argv[3]
    
    with open(arquivo_entrada, 'r', encoding='utf-8') as f:
        texto = f.read()
    
    if modo in ['cifrar', 'decifrar']:
        if len(sys.argv) < 5:
            print("Erro: Chave não fornecida")
            return
        
        chave = sys.argv[4]
        resultado = cifrar_vigenere(texto, chave, modo)
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(resultado)
        
        print(f"Operação {modo} concluída. Resultado em {arquivo_saida}")
    
    elif modo == 'kasiski':
        resultados = analise_kasiski(texto)
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            if resultados:
                f.write("Possíveis tamanhos de chave (método Kasiski):\n")
                for tamanho, freq in resultados:
                    f.write(f"- {tamanho} (frequência: {freq})\n")
            else:
                f.write("Não foram encontrados padrões repetidos suficientes para análise Kasiski.\n")
        
        print(f"Análise Kasiski concluída. Resultados em {arquivo_saida}")
    
    else:
        print("Modo inválido. Use 'cifrar', 'decifrar' ou 'kasiski'")

if __name__ == "__main__":
    main()