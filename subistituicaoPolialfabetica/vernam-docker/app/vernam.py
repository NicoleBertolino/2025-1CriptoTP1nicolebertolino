import base64
import sys

def ler_arquivo(nome_arquivo):
    """Lê o conteúdo de um arquivo em modo texto"""
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return f.read()

def ler_chave(nome_arquivo):
    """Lê a chave do arquivo CHAVE.txt"""
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return f.read().strip()

def aplicar_vernam(texto, chave):
    """Aplica a cifra de Vernam (XOR) entre texto e chave"""
    texto_bytes = texto.encode('utf-8')
    chave_bytes = chave.encode('utf-8')
    
    # Repete a chave até atingir o tamanho do texto
    chave_repetida = (chave_bytes * (len(texto_bytes) // len(chave_bytes) + 1))[:len(texto_bytes)]
    
    # Aplica XOR byte a byte
    resultado = bytes([a ^ b for a, b in zip(texto_bytes, chave_repetida)])
    return resultado

def main():
    if len(sys.argv) != 2:
        print("Uso: python vernam.py <arquivo_chave>")
        return
    
    arquivo_chave = sys.argv[1]
    
    try:
        # 1. Ler texto claro e chave
        texto = ler_arquivo('CLARO.txt')
        chave = ler_chave(arquivo_chave)
        
        # 2. Aplicar cifra de Vernam
        resultado_xor = aplicar_vernam(texto, chave)
        
        # 3. Salvar resultado bruto (possivelmente ilegível)
        with open('VernamRAW.txt', 'w', encoding='utf-8', errors='replace') as f:
            f.write(resultado_xor.decode('utf-8', errors='replace'))
        
        # 4. Salvar em binário puro
        with open('VernamBin.txt', 'wb') as f:
            f.write(resultado_xor)
        
        # 5. Tentar decodificar para UTF-8 (geralmente falha)
        try:
            texto_decodificado = resultado_xor.decode('utf-8')
            with open('VernamUtf8.txt', 'w', encoding='utf-8') as f:
                f.write(texto_decodificado)
        except UnicodeDecodeError:
            with open('VernamUtf8.txt', 'w') as f:
                f.write("Não foi possível decodificar o resultado como UTF-8 válido")
        
        # 6. Codificar em Base64 para visualização segura
        base64_result = base64.b64encode(resultado_xor).decode('ascii')
        with open('VernamBase64.txt', 'w') as f:
            f.write(base64_result)
        
        print("Operação concluída. Arquivos gerados:")
        print("- VernamRAW.txt (resultado bruto, possivelmente ilegível)")
        print("- VernamBin.txt (binário puro)")
        print("- VernamUtf8.txt (tentativa de decodificação UTF-8)")
        print("- VernamBase64.txt (versão codificada em Base64)")
    
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()