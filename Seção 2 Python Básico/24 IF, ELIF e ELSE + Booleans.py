"""
Condições IF, ELIF (else + if), ELSE

A menos que cada bloco seja verdadeiro, o if irá testar bloco a bloco, ou seja,
se a cada verificação feita não encontrar a condição "True", a verificação pula
para o bloco seguinte e caso nao encontre, será executado o else final.

As condições podem ser encadeadas;
As condições verdadeira (True) e falsa (False), obrigatoriamente devem iniciar com letras maiúsculas.

"""

if False:
    print('verdadeiro.')
elif True:
    print("Agora é verdadeiro.")
    nome = input("Qual o seu nome? ")
    print(f'Seu nome é {nome}.')
elif False:
    print('Mais uma verdadeira.')
    print(22 + 22)
else:
    print("Não é verdadeiro.")
    print("olá")
