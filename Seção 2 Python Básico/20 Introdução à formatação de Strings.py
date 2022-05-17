"""
Introdução a formatação de Strings.

Para formatar casas decimais (:.2f), para duas casas após a vírgula.
"""

nome = 'Eugues'
idade = 33
altura = 1.98
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
