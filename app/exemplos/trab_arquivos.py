import subprocess
#arquivo = open("app\exemplos\dados.txt","r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close
#escrita

try:
   

    with open("app\exemplos\dados.txt","r") as arquivo:
         conteudo = arquivo.read()
         print(conteudo)

except FileNotFoundError:
    print(" Arquivo não encontrado")

#sobreescrita
with open("app\exemplos\dados.txt","w") as arquivo:
   arquivo.write("Bem vindo ao python")

#adiionar novo conteudo
with open("app\exemplos\dados.txt","a") as arquivo:
   arquivo.write(" Usuario logado\n")
   
# abrindo em uma das minhas escolhas 
import os
os.startfile(r"c:\Users\oliveira.paola\Documents\GitHub\pythonUC3\app\exemplos\dados.txt")