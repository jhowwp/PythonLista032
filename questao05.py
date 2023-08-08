'''
5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao1 = numero1 - numero2
subtracao2 = numero2 - numero1
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
    resto_divisao = numero1 % numero2
else:
    divisao = "Divisão por zero não é possível"
    resto_divisao = "Divisão por zero não é possível"

print(f"Soma: {soma:.2f}")
print(f"Subtração do primeiro pelo segundo: {subtracao1:.2f}")
print(f"Subtração do segundo pelo primeiro: {subtracao2:.2f}")
print(f"Multiplicação: {multiplicacao:.2f}")
print(f"Divisão do primeiro pelo segundo: {divisao}")
print(f"Resto da divisão do primeiro pelo segundo: {resto_divisao}")
