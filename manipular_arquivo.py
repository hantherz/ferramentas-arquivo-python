# funções de mover, copiar, ler, deletar, escrever em um arquivo e procurar um arquivo

import shutil
from pathlib import Path

print("--------------------MENU DE FUNÇÕES--------------------")
print(f"INÍCIO PADRÃO: {Path.home()}")
print("1 - Mover | 2 - Copiar | 3 - Ler | 4 - Criar | 5 - Deletar | 6 - Escrever | 7 - Procurar")

arquivo = str(input("Arquivo: "))
pesquisa_dir_atual = Path.glob(Path.home(), arquivo)
arquivos = []
i_arq = 0

if(pesquisa_dir_atual == True):
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
    escolher_arquivo = int(input("Opção: "))
    print(arquivos[escolher_arquivo - 1])
