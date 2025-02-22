a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))

op = input("Digite a operação desejada: + , - , * , / : ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a/b)
else:
    print("digite uma operação válida")