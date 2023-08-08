'''
1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom
'''
valor_conta = (floatinput("Digite o valor da conta: "))

gorjeta = valor_conta * 0.10

total_a_pagar = valor_conta + gorjeta

print(f"Valor da conta: R${valor_conta:.2f}")
print(f"Gorjeta (10%): R${gorjeta:.2f}")
print(f"Total a pagar: R${total_a_pagar:.2f}")




