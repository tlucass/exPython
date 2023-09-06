#Lucas P. de Toledo
#RM: 97913

ditado = input('Digite um ditado popular: ')
nomeArq = input('Digite um nome para o arquivo: ')

try:
    arqCriado = open(f'd:/{nomeArq}.txt', 'w', encoding='utf-8')
    arqCriado.write(ditado)
    arqCriado.close()

    arqCriado = open(f'd:/{nomeArq}.txt', 'r')
    print(arqCriado.read())
    arqCriado.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')




ditado2 = input('Agora, digite um outro ditado para adicionar ao arquivo já criado: ')

try:
    outroDitado = open(f'd:/{nomeArq}.txt', 'a', encoding='utf-8')
    outroDitado.write(f'\n{ditado2}')
    outroDitado.close()

    outroDitado = open(f'd:/{nomeArq}.txt', 'r')
    print(outroDitado.read())
    outroDitado.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')
