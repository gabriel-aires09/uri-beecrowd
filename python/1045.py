a, b, c = map(float, input().split())

tmp = [a, b, c]
reverse = sorted(tmp, reverse=True)

A = reverse[0]
B = reverse[1]
C = reverse[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
elif (pow(A, 2)) == (pow(B, 2)) + (pow(C,2)):
    print("TRIANGULO RETANGULO")
elif (pow(A, 2)) > (pow(B, 2)) + (pow(C, 2)):
    print("TRIANGULO OBTUSANGULO")
elif (pow(A, 2)) < (pow(B, 2)) + (pow(C, 2)):
    print("TRIANGULO ACUTANGULO")
if (A == B) and (B == C):
    print("TRIANGULO EQUILATERO")
elif ((A == B or B == C) and not (A == B and B == C) and reverse):
    print("TRIANGULO ISOSCELES")
