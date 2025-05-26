#Como cria matrizes
A = [[1,2],
      [4,5]]
B = [[2,3],
     [5,6]]
print(A[0][1])
# A[linha][coluna], parecido com o conceito de branch 
print(len(A)) # len é a quantidade de linhas
print(len(A[0]))# é a quantidade de colunas, ou seja len  e acessando um número, descobrimos a quantidade de colunas
Matriz_soma = []
for linhas in range(len(A)):
    l_Matriz_soma = []
    for colunas in range(len(A[0])):
        soma = A[linhas][colunas] + B[linhas][colunas]
        l_Matriz_soma.append(soma)
    Matriz_soma.append(l_Matriz_soma)
print(Matriz_soma)

