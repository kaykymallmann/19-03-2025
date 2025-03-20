def ler_arquivo(nome_arquivo): 
    try:
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError:
        print("Erro ao ler o arquivo.")
    return None

print(ler_arquivo("dados.txt"))
