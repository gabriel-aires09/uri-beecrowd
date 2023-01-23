a, b, c = map(float, input().split())

if ((b - c) < a) and (a < (b + c) ):
    print("Perimetro = {}".format(a + b + c))
else:
    print("Area = {}".format((a + b) * c/2))

