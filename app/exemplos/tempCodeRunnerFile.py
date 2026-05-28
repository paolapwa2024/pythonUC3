# jogo da forca professor.

import os
palavra_secreta = "perfume"
letra_acertos = " "
numero_tentattivas = 0
letras_erradas = " "

while True:
    letra_digitadas = input("Digite uma letra:")
    letra_digitadas = letra_digitadas.lower()
    numero_tentattivas += 1

    if letra_digitadas in letra_acertos:
        print("Você ja acertou essa letra")
        continue

    if letra_digitadas in letras_erradas:
        print("letra errada")
        continue

    if len (letra_digitadas)>1:
        print("Digite apenas um letra:")
        continue

    if letra_digitadas in palavra_secreta:
       letra_acertos += letra_digitadas
       print(" letra certa")

    else:
       print("Letra incorreta")
       letras_erradas += letra_digitadas

       palavra_formada = " "
       for letra_acertos in palavra_secreta:
           if palavra_secreta in letra_acertos:
               palavra_formada += palavra_secreta
           else:
               palavra_formada += "*"
    
    print("\n===================================================")
    print("palavra:",palavra_formada)
    print('letras erradas:', letras_erradas)
    print("tentativas", numero_tentattivas)
    print('=======================================================\n')

    if palavra_formada == palavra_secreta:
        os.system("cls" if os.name == "nt" else "clear")
        print("oce ganhou!")
        print(f"A palabra secreta era:{palavra_secreta}")
        print(f"Total de tentativas: {numero_tentattivas}")


        break

print("\n Jogo acabou.")
    