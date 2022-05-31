from Exercícios.Mundo3.ex115.lib.interface import *
from Exercícios.Mundo3.ex115.lib.arquivo import *
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'sair do sistema'])
    if r == 1:
        lerArquivo(arq)
    elif r == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif r == 3:
        print('Saindo do sistema')
        break
    else:
        print('Erro didgite uma opçao valida')