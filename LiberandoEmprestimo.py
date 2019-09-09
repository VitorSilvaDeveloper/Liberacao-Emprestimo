from time import sleep

nome = str(input('Qual o seu nome completo,por favor?'))
salario = float(input('Qual o seu salário? R$'))
emprestimo = float(input('Quanto você quer pegar emprestado? R$'))
mensalidade = float(input('Em quantos meses deseja pagar?'))

str(input('CASO O EMPRESTIMO FOR APROVADO, CORRERA UM JUROS DE 6% A.M \nO VALOR DO JUROS SERÁ INCLUSO JÁ NO VALOR NA MENSALIDADE \nAperte Enter para continuar!'))

print('{}, só um momento!'.format(nome))
sleep(0.5)
print('Verificando...')
sleep(1)
print('Processando...')
sleep(1)
print('Validando processo...')
sleep(2)

resultado1 = emprestimo / mensalidade
resultado2 = salario - (salario * 70 / 100)

if resultado1 <= resultado2:
    valor_final = resultado1 + (resultado1 * 6 / 100)
    print('PARABÉNS! Seu emprestimo foi aprovado!')
    print('Valor aproximado das suas parcelas ficou de R${:.2f} com acrescimo de 6% por mês de juros!'.format(valor_final))

else:
    print('Infelizmente não podemos liberar esse valor emprestado agora. \nTente um valor mais baixo ou a mensalidade excedeu o limite de 30% do seu salário!')

print('by VITOR SILVA')
