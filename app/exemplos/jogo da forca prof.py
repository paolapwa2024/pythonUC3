# jogo da forca professor.

palavra_secreta = "perfume"
letra_acertos = " "
numero_tentattivas = 0
letras_errdas = " "

while True:
    letra_digitadas = input("Digite uma letra:")
    letra_digitadas = letra_digitadas.lower()
    numero_tentattivas += 1

    if letra_digitadas in letra_acertos:
        print("Você ja acertou essa letra")
        continue

    if letra_digitadas in letras_errdas:
        print("letra errada")
        continue

    if len (letra_digitadas)>1:
        print("Digite apenas um letra:")
        continue

    if letra_digitadas in palavra_secreta:
       letra_acertos += letra_digitadas
       print(" letra certa")

       palavra_formada = " "