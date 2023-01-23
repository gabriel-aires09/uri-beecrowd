A, B, C = map(float, input().split())

delta = ((B ** 2) -4 * A * C)

if ((delta < 0) or (A == 0)):
    print("Impossivel calcular")

elif (delta == 0):
    R1 = (-B + delta ** 0.5) / (2 * A)
    R2 = R1
    print("R1 = %0.5f" % R1)
    print("R2 = %0.5" % R2)

else:
    R1 = (-B + delta ** 0.5) / (2 * A)
    R2 = (-B - delta ** 0.5) / (2 * A)
    print("R1 = %0.5f" % R1)
    print("R2 = %0.5f" % R2)
