"""
Entrada de dados em Python, sempre retornará uma String,
para que a entrada se comporte de maneira diferente, por exemplo,
como um número, precisamos fazer o "cast" que é transformar uma String em um número
desta forma => int(input("Digite um número? "))
"""

nome = input("Qual o seu nome? ")
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')


numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite um número: ')
numero_2 = int(numero_2)

print(numero_1 + numero_2)
print(numero_1 ** numero_2)





