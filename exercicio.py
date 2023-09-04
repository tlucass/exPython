#Lucas P. de Toledo
#RM: 97913

ditado = input('Digite um ditado popular: ')
nomeArq = input('Digite um nome para o arquivo: ')

try:
    arqCriado = open(f'd:/{nomeArq}.txt', 'w')
    arqCriado.write(ditado)
    arqCriado.close()

    arqCriado = open(f'd:/{nomeArq}.txt', 'r')
    print(arqCriado.read())
    arqCriado.close()
except FileNotFoundError:
    print('Arquivo não encontrado!')