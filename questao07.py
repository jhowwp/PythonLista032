'''
7) A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações
'''

# Solicita o valor da compra e o número de prestações ao usuário
valor_compra = float(input("Digite o valor da compra: "))
numero_prestacoes = int(input("Digite o número de prestações desejado (1 a 10): "))

# Calcula o valor das prestações (divide o valor da compra pelo número de prestações)
valor_prestacao = valor_compra / numero_prestacoes

# Exibe os resultados
print(f"Valor da compra: R${valor_compra:.2f}")
print(f"Número de prestações: {numero_prestacoes}")
print(f"Valor de cada prestação: R${valor_prestacao:.2f}")


