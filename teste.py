#Como cria matrizes
def criar():
     A = [] #Matriz vazia 
     l,c = map(int,input("Insira a quantidade de linhas {l} e de {c} que você deseja").split())
     for linhas in range(l):
      New_matriz =[]
      for colunas in range(c):
        number = int(input("insira o número desejado"))
        New_matriz.append(number)
      A.append(New_matriz)
     return A
print(len(criar()))
def multiplicacao(multium,multidois):
   D = str(input(""))