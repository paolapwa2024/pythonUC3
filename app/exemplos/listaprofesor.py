#professor

nome = "bruno"
listaNomes = ["ana","brenda", "bruna","taissa"]
print(nome)
print (listaNomes)
print(len(listaNomes))#contar quantos elementos existem
listaNomes.append ("luisa")# adicionar umnovo item
print(listaNomes)
print(listaNomes.index("brenda"))#recuperar um idex pesquisado
nova_lista = [1,5,"dog",10,"gato"]# lista heterogenea
print(nova_lista)
nova_lista.remove(5)
#nova_lista.remover(5)#remover item de lista
nova_lista.reverse()
print(nova_lista)#reverter os nomes da lista
nova_lista.append([10,56,9])#adicionar uma lsita dentro de outra lista
numeros = [5,3,1,4,2]
print(numeros.sort()) #ordenados crescente
numeros.sort(evere=True) # ordenado decrescente

listaNumeros2 = numeros.copy()

#fatia lista
n1 = numeros[0]
n2 = numeros[1]

#ou
print(numeros[0:3])




