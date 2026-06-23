def soma(num1,num2):
    total = num1 + num2
    return total

def exebirmg():
    print("isso é uma função")


def exebirmg2():
    return("isso é uma função")


#temp = soma()
print(soma(5, 6))


print(exebirmg2())
exebirmg()


def test(senha):
    if senha == "12345":
        print("Senha correta")
    else:
        print("Senha incorreta")


test (input("Digite a senha:\n "))


def contnum(num):
    for i in range(1, num + 1):
        print(i)


contnum(5)

def contwhile():
    count = 0
    while count < 3:
        print(count)
        count += 1

contwhile ()