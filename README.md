# Ferramentas para a Manipulação de Arquivos em Python
---
## Para que serve?
É uma função principal que contém "subfunções" para manipular **arquivos, não pastas**, e que estão prontas para integração com outros programas. O próprio programa busca os arquivos a partir da pasta home do seu sistema operacional (adaptado para linux, mas funciona em windows também) e retorna todos os resultados, escolha uma das opções, caso haja mais de uma com o mesmo nome, e ele definirá o que **você escolheu**. **Isso vale para tudo**, exceto a criação de arquivos, que pede o nome e o diretório de destino.

## Quais funções estão presentes?
- Mover
   * Move um arquivo de um diretório para outro. Informe o ficheiro e o caminho de destino.
- Copiar
   * Copia um arquivo com seus metadados e permissões de um diretório para outro. Informe o ficheiro e o caminho de destino.
- Ler
   * Lê e mostra o que há dentro. Não faz leitura de arquivos binários.
- Criar
   * Cria um arquivo novo. Informe seu nome e o diretório onde ele será criado.
- Deletar
   * Deleta um arquivo. Informe seu nome para que possa deletá-lo.
- Escrever
   * Escreve em um arquivo sem apagar o que já está escrito (não sobrescreve), adicionando o texto ao final.
- Procurar
   * Faz uma varredura em busca do arquivo a partir do caminho padrão (home) do seu sistema operacional e lista as opções.
