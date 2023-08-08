'''
8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.
 Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário
'''


preco_custo = float(input("Digite o preço de custo do produto: "))
percentual_acrescimo = float(input("Digite o percentual de acréscimo: "))

valor_venda = preco_custo * (1 + percentual_acrescimo / 100)

print(f"Preço de custo: R${preco_custo:.2f}")
print(f"Percentual de acréscimo: {percentual_acrescimo}%")
print(f"Valor de venda: R${valor_venda:.2f}")
