'''
2) Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia.
'''


hora_atual = int(input("Digite a hora atual: "))
minutos_atual = int(input("Digite os minutos atuais (0-59): "))

minutos_passados = hora_atual * 60 + minutos_atual

print(f"Desde 00:00h até {hora_atual:02d}:{minutos_atual:02d} se passaram {minutos_passados} minutos.")