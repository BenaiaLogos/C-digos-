N,K = map(int,input("insira os valores de N e K").split())
A = list(map(int,input().split()))
Nova_lista = A 
B = list(map(int,input().split()))
D = sorted(A)
vazia = A.index(len(A))
print(vazia)
dados = A.pop(len(A))
print(dados)
if D[0]== A[0]:
    print("função crescente")

        
elif D[0] != A[0]:
    print("função decrescente")

print(sorted(A,key=int))
print(B)
print(Nova_lista)