# funções de mover, copiar, ler, deletar, escrever em um arquivo e procurar um arquivo

import shutil
from pathlib import Path

def localizar_arquivo():
    arquivo = str(input("Arquivo: "))
    pesquisa_dir_atual = Path.glob(Path.home(), arquivo)
    arquivos = []
    i_arq = 0

    if(pesquisa_dir_atual):
        for arquivo in pesquisa_dir_atual:
            arquivos.append(arquivo)
            print(f"{i_arq + 1}: {arquivo}")
            i_arq += 1
    else:
        pesquisa_subdirs = Path.rglob(Path.home(), arquivo)
        for arquivo in pesquisa_subdirs:
            arquivos.append(arquivo)
            print(f"{i_arq + 1}: {arquivo}")
            i_arq += 1
    if(len(arquivos) > 1):
        escolher_arquivo = int(input("Opção: "))
        arquivo = arquivos[escolher_arquivo - 1]
        return arquivo
    else:
        return arquivo

def caminho_destino():
    output = str(input(f"Caminho de saída: {Path.home()}/"))
    outputpath = Path.home() / output
    return outputpath

print("--------------------MENU DE FUNÇÕES--------------------")
print(f"INÍCIO PADRÃO: {Path.home()}")
print("1 - Mover | 2 - Copiar | 3 - Ler | 4 - Criar | 5 - Deletar | 6 - Escrever | 7 - Procurar")

opcao = str(input("Função (use o número referente): "))

if(opcao == "1"):
    arquivo = localizar_arquivo()
    path_destino = caminho_destino()
    shutil.move(arquivo, path_destino)
    print("Arquivo movido.")
elif(opcao == "2"):
    arquivo = localizar_arquivo()
    path_destino = caminho_destino()
    shutil.copystat(arquivo, path_destino)
    print("Arquivo copiado.")
elif(opcao == "3"):
    arquivo = localizar_arquivo()
    if(arquivo.stat().st_size == 0):
        print("Arquivo vazio.")
    else:
        print(Path.read_text(arquivo))
elif(opcao == "4"):
    arquivo = str(input("Novo arquivo: "))
    path_destino = caminho_destino()
    path_destino = path_destino / arquivo
    Path.touch(path_destino)
    print("Arquivo criado.")
elif(opcao == "5"):
    arquivo = localizar_arquivo()
    Path.unlink(arquivo)
    print("Arquivo deletado.")
elif(opcao == "6"):
    arquivo = localizar_arquivo()
    texto = str(input("Texto a ser inserido ao final do arquivo: "))
    with open(arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto)
    print("Texto inserido.")
elif(opcao == "7"):
    print(localizar_arquivo())