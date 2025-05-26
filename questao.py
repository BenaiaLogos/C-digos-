C,G = map(int,input().split())
C = min(max(C,0),1)
G = min(max(G,0),1)
if C == 0:
    if G == 1:
        print("vivo")
    elif G == 0:
        print("morto")
else:
    print("vivo e morto")