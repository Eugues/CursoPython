"""
Operadores Relacionais
== Igual
>  Maior
>= Maior ou igual
<  Menor
<= Menor ou igual
!= Diferente

Para ocorrer a comparação os tipos primitivos devem ser do mesmo tipo;

"""

"""
num_1 = 2
num_2 = 2

#   Igual a "=="
print(f'\n\nIgual a "==": ', end='')
print(f'2 é igual a 2 =>', num_1 == num_2)

#   Maior que ">"
print(f'\nMaior que ">": ', end='')
print(f'2 é Maior que 2 =>', num_1 > num_2)

#   Maior ou igual ">="
print(f'\nMaior ou igual ">=": ', end='')
print(f'2 é Maior ou igual a 2 >=', num_1 >= num_2)

#   Menor "<"
print(f'\nMenor que "<": ', end='')
print(f'2 é Menor que 2 =>', num_1 < num_2)

#   Menor ou igual "<="
print(f'\nMenor ou igual "<=": ', end='')
print(f'2 é Menor ou igual a 2 =>', num_1 <= num_2)


#   Diferente "!="
print(f'\nDiferente ">=": ', end='')
print(f'2 é Diferente de 2 =>', num_1 != num_2)

"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade_limite = 18
idade = int(idade)
"""
# Limite para pegar empréstimo 01   

if idade >= idade_limite:
    print(f'{nome}pode pegar empréstimo.')
else:
    print(f'{nome} Não pode pegar empréstimo')

"""

# Limite para pegar empréstimo 2
idade_menor = 20    # Muito jovem
idade_maior = 30    # Passou da idade

if idade_menor <= idade < idade_maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar empréstimo')
