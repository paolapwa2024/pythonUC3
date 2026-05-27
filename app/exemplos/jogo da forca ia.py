palavra_secreta = "gato"
letras_acertadas = []
letras_erradas = []
tentativas_maximas = 6

print("=== JOGO DA FORCA ===")
print(f"A palavra tem {len(palavra_secreta)} letras.")
print("_ " * len(palavra_secreta), "\n")

while True:
    #
    tentativas_restantes = tentativas_maximas - len(letras_erradas)
    print(f"Tentativas restantes: {tentativas_restantes}/{tentativas_maximas}")

    
    if letras_erradas:
        print(f"Letras erradas: {' / '.join(letras_erradas)}")

    
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

    
    if all(letra in letras_acertadas for letra in palavra_secreta):
        print("Parabens! Voce acertou a palavra:", palavra_secreta)
        break

   
    if tentativas_restantes == 0:
        print("Suas tentativas acabaram! A palavra era:", palavra_secreta)
        break

   
    chute = input("Digite uma letra: ").lower()

   
    if chute in letras_acertadas or chute in letras_erradas:
        print("Voce ja tentou essa letra!\n")
        continue

    
    if chute in palavra_secreta:
        letras_acertadas.append(chute)
        print(f"Letra '{chute}' esta na palavra!\n")
    else:
        letras_erradas.append(chute)
        print(f"Letra '{chute}' NAO esta na palavra!\n")