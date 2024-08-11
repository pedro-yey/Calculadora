n1 = float(input("Me fale um número: "))
n2 = float(input("Me fale um outro número: "))
operador = input("Selecione o operador desejado: +, - , x, /")

if operador == '+':
    print(n1 + n2)
elif operador == '-':
    print(n1 - n2)
elif operador == 'x':
    print (n1*n2)
elif operador == '/':
    print (n1/n2)
else:
    print('Operador errado!')
