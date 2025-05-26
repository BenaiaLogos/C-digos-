
while True:
   N = int(input())
   N = min(max(N,10),10**5)
   S = str(input().split())
   T = str(input().split())
   Linguas = []
   Letras = []
   contador_um = 0
   contador_dois = 0
   for numeros in S:
     if numeros is not numeros.isdigit():
       Linguas.append(numeros)
   for elementos in T:
    if elementos is not elementos.isdigit():
      Letras.append(elementos)
   for astericos in Letras:
     if astericos == "*":
      contador_um+=1
   for Astericos in Linguas:
    if Astericos == "*":
      contador_dois+=1
   if contador_um > N or contador_dois> N:
       continue
   sub = contador_dois - contador_um
   razao = ((f"{sub/contador_dois:.2f}"))
   print(razao)