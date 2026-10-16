# funções de mover, copiar, ler, deletar, escrever em um arquivo e procurar um arquivo

import shutil
from pathlib import Path

stdpath = Path.home()

print("MENU DE FUNÇÕES".center)
print(f"INÍCIO PADRÃO: {Path.home()}")
print("1 - Mover | 2 - Copiar | 3 - Ler | 4 - Criar | 5 - Deletar | 6 - Escrever | 7 - Procurar")

funcao = str(input("Função: "))

if(funcao == "1"):
    arquivo = str(input("Arquivo: "))
    outputpath = str(input("Diretório do arquivo: "))
    arquivo_path = stdpath / outputpath / arquivo
    shutil.move(arquivo, arquivo_path)
    print("Arquivo movido.")
elif(funcao == "2"):
    arquivo = str(input("Arquivo: "))
    outputpath = str(input("Diretório do arquivo: "))
    arquivo_path = stdpath / outputpath / arquivo
    shutil.copystat(arquivo, outputpath)
    print("Arquivo copiado.")
elif(funcao == "3"):
    arquivo = str(input("Arquivo: "))
    outputpath = str(input("Diretório do arquivo: "))
    arquivo_path = stdpath / outputpath / arquivo
    shutil.copystat(arquivo, outputpath)
    print(Path.read_text(arquivo_path))
elif(funcao == "4"):
    arquivo = str(input("Arquivo novo: "))
    outputpath = str(input("Criar arquivo em: "))
    arquivo_path = stdpath / outputpath / arquivo
    Path.touch(arquivo_path)
    print("Arquivo vazio criado.")
elif(funcao == "5"):
    arquivo = str(input("Arquivo: "))
    outputpath = str(input("Diretório do arquivo: "))
    arquivo_path = stdpath / outputpath / arquivo
    arquivo_path.unlink(missing_ok=True)
    print("Arquivo deletado.")
elif(funcao == "6"):
    arquivo = str(input("Arquivo: "))
    outputpath = str(input("Diretório do arquivo: "))
    texto = str(input("Escreva: "))
    arquivo_path = stdpath / outputpath / arquivo
    Path.write_text(texto, arquivo_path)
    print("Arquivo sobrescrito.")
elif(funcao == "7"):
    arquivo = str(input("Arquivo: "))
    check_stdpath = str(input(f"Procurar a partir de {stdpath} (1 - Sim | 0 - Não): "))
    if(check_stdpath == "0"):
        path = str(input("Procurar a partir de: "))
        path = path
        localizacao = Path.rglob(path, arquivo)
    localizacao = Path.rglob(stdpath, arquivo)
    for resultado in localizacao:
        print(resultado)
    