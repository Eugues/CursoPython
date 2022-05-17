"""
* Criar variáveis para: nome (str), idade (int), altura (float), peso (float) de uma pessoa;
* Criar variável com ano atual (int.);
* Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual);
* Obter o Índice de Massa Corporal com duas casas decimais (no peso e na altura das pessoas);
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Eugues'
altura = 1.98
peso = 114
ano_atual = 2022
nascimento = 1984
idade = ano_atual - nascimento
imc = peso / altura ** 2

print(f'Eugues tem {idade} anos, {altura:.2f} de altura e pesa {peso}kg.')
print(f'O IMC de Eugues é {imc:.2f}.')
print(f'Eugues nasceu em {nascimento}.')
