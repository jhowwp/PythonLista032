'''
9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias
'''


anos = int(input("Digite a quantidade de anos:"))
meses = int(input("Digite a quantidade de meses:"))
dias = int(input("Digite a quantidade de dias:"))


idade_em_dias = anos * 365 + meses * 30 + dias


print(f"A idade expressa em dias é: {idade_em_dias} dias")
