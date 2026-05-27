# === JOGO DA FORCA SIMPLES ===
 
palavra = "gato"
erros = 0
acertadas = []
 
print("Adivinhe a palavra!")
 
while True:
 
    for letra in palavra:
        if letra in acertadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
 
    print() 
 
    
    if all(letra in acertadas for letra in palavra):
        print("Parabens! A palavra era:", palavra)
        break
 
    
    if erros == 6:
        print("Voce perdeu! A palavra era:", palavra)
        break
 
    
    chute = input("Digite uma letra: ").lower()
 
    
    if chute in palavra:
        acertadas.append(chute)
        print("Acertou!\n")
    else:
        erros = erros + 1
        print(f"Errou! Erros: {erros}/6\n")
