"""
Operações Básicas
+   =>  soma
-   =>  subtração
*   =>  multiplicação
/   =>  divisão

Operações específicas
//  =>  divisão de números inteiros (arredondamento)
**  =>  Exponenciação
%   =>  resto da divisão
( ) =>  precedência

"""
print("Adição '+' \n2 + 2 =", 2 + 2)
print("\nSubtração '-' \n2 - 2 =", 2 - 2)
print("\nMultiplicação '*' \n2 * 2 =", 2 * 2)
print("\nDivisão Números reais (com virgula) '/' \n2 / 2 =", 2 / 2)
print("\nDivisão de números inteiros '//' \n2 // 2 =", 2 // 2)
print("\nExponenciação '**' \n2 ** 2 =", 2 ** 2)
print("\nResto da divisão '%' \n2 % 2 =", 2 % 2)
print("\nPrecedência '()' \n(1 + 1) * 5 =", (1 + 1) * 5)

"""
    Assim como aprendemos na matemática, operadores têm uma certa precedência 
que pode ser alterada usando os parênteses.

    Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade
na hora de realizar contas mais complexas (de maior para menor precedência).
    
    1. ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
    2. ** - Depois vem a exponenciação 
    3. *, /, //, % - Na sequência multiplicação, divisão, divisão inteira e módulo (resto da divisão)
    4. +, - - Por fim, soma e subtração
    
    Contas com operadores de mesma precedência são realizadas da esquerda para a direita.
    
    Observação: existem muito mais operadores do que estes em Python
e todos eles também têm precedência, você pode ver a lista completa em 
https://docs.python.org/3/reference/expressions.html#operator-precedence 
(sempre utilize a documentação oficial como reforço caso necessário)
    
    Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta
e tente decifrar como chegar no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0). 
Para isso você precisa realizar as contas com maior precedência primeiro.
    
"""