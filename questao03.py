'''
3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

peso_kilos = float(input("Digite o seu peso em quilos: "))
altura_metros = float(input("Digite a sua altura em metros: "))


peso_gramas = peso_kilos * 1000
altura_centimetros = altura_metros * 100


print(f"Seu peso em gramas é: {peso_gramas:.2f} g")
print(f"Sua altura em centímetros é: {altura_centimetros:.2f} cm")
print("Obrigado pela sua informação")
