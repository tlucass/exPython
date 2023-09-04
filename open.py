# try: 
#     r = open('d:/rato.txt', 'r')
#     print(r.readline())
#     r.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")







# try: 
#     r = open('d:/rato.txt', 'r')
#     for i in range(1, 5, 1):
#         print(r.readline())
#     r.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")








# try: 
#     r = open('d:/rato.txt', 'a')
#     r.write("\nabcde")
#     r.close()

#     r = open('d:/rato.txt', 'r')
#     print(r.read())
#     r.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")





# try: 
#     r = open('d:/rato.txt', 'w')
#     r.write("Batatinha quando nasce")
#     r.write("\nEspalha rama")
#     r.write("\npelo chão")
#     r.close()

#     r = open('d:/rato.txt', 'r')
#     print(r.read())
#     r.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")





# try: 
#     r = open('d:/batatinha.txt', 'x')
#     r.close()

#     r = open('d:/batatinha.txt', 'a')
#     r.write("Batatinha quando nasce")
#     r.close()
    

#     r = open('d:/batatinha.txt', 'r')
#     print(r.read())
#     r.close()
# except FileNotFoundError:
#     print("Arquivo não encontrado")


import os
try: 
    if os.path.exists('d:/trigres.txt'):
        os.remove('d:/trigres.txt')

    f = open('d:/trigres.txt', 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('Arquivo não encontrado')