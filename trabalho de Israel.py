conta = []
proprietario = []
saldo = []

def cadrasto(numero,contas):
    conta.append(numero)
    proprietario.append(contas)
    saldo.append(0)
    return "conta cadrastada com sucesso"


def verificar():
    cont = 0
    while cont < len(conta):
        print(conta[cont])
        print(saldo[cont])
        print(proprietario[cont])
        cont += 1


def deposito(numero):
    if numero in conta:
        valor = float(input("qual o valor a ser depositado?"))
        posicao = conta.index(numero)
        saldo[posicao] = (saldo[posicao]) + valor
        return "deposito realizado com sucesso"
    else:
        return "conta inexistente"
    

def saque(numero):
    if numero in conta:
        valor = float(input("qual o valor a ser sacado?"))
        posicao = conta.index(numero)
        saldo[posicao] = (saldo[posicao]) - valor
        return "saque realizado com sucesso"
    else:
        return "conta inexistente"

def transferencia(num1, valor1, num2):
    if num1 in conta:
        posicao = conta.index(num1)
        saldo[posicao] = (saldo[posicao]) - valor1
        if num2 in conta:
            posicao2 = conta.index(num2)
            saldo[posicao2] = (saldo[posicao2]) + valor1



op = 1
while op != 0:
    op = int(input("em que posso lhe ajudar?"+
                    "\n1 - cadrastar uma conta"+
                    "\n2 - verificar o saldo existente"+
                    "\n3 - adcione um saldo"+
                    "\n4 - sacar o dinheiro"+
                    "\n5 - transferir o dinheiro"))
    

    if op == 1:
        num = int(input("digite um numero para a conta que deseja"))
        nome = str(input("digite seu nome")) 
        print("este e o seu saldo, 0!")
        cadrasto(num, nome)
    elif op == 2:
        verificar()
    elif op ==3:
        numConta = int(input("qual sua conta?"))
        deposito(numConta)
    elif op ==4:
        numconta = int(input("qual o numero da conta a ser sacado?"))
        saque(numConta)
    elif op ==5:
        numero = int(input("qual o numero da conta a ser transferido o dinheiro?"))
        valor2 = float(input("digite o valor que queira transferir"))
        num2 = int(input("qual o numero da conta para transferir o dinheiro?"))
        transferencia(numero, valor2, num2)
        

       



