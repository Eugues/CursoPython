"""
print as variáveis e calcule o IMC

"""

nome = 'Eugues'
idade = 33
altura = 1.98
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)
print(imc)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Maior de idade:', e_maior)

print(nome, ' tem', idade, ' anos de idade e seu imc e igual a', imc)
