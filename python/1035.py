selecao = input().split(" ")
A, B, C, D = selecao
somaCD = C + D
somaAB = A + B
split = selecao
A = int(split[0])
B = int(split[1])
C = int(split[2])
D = int(split[3])

if (B > C):
    if (D > A):
        if (somaCD > somaAB):
            if ((C > 0) and (D > 0)):
                if (A % 2 == 0):
                    print("Valores aceitos")
else:
    print("Valores nao aceitos")
