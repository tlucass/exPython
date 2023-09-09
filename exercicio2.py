#Lucas P. de Toledo
#RM: 97913

import os

numerosPares = {0}
numerosPares.remove(0)

if os.path.exists('d:/numPares.txt'):
    os.remove('d:/numPares.txt')

arquivo = open('d:/numPares.txt', 'x', encoding='utf-8')
arquivo.close()

while True:
    try:
        nums = int(input("Digite números inteiros (pressione (0) para parar.): "))
        numerosPares.add(nums)
    

        if nums % 2 == 0:
            pares = nums
            if pares != 0:
                try:
                    arquivo = open('d:/numPares.txt', 'a', encoding='utf-8')
                    arquivo.write(f"{str(pares)}\n")
                    arquivo.close()
                except FileNotFoundError:
                    print('Arquivo não encontrado!')
    

        if nums == 0:
            numerosPares.remove(0)
            print(f"Set:{numerosPares}")

            arquivo = open('d:/numPares.txt', 'r')
            print(arquivo.read())
            arquivo.close()
            break

    except ValueError:
        print("Digite um valor válido!")
        break