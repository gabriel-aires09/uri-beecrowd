LINE1 = input().split(" ")
LINE2 = input().split(" ")

code1, qtde1, value1 = LINE1
code2, qtde2, value2 = LINE2

PRODUCT1 = int(qtde1) * float(value1)
PRODUCT2 = int(qtde2) * float(value2)
TOTAL = PRODUCT1 + PRODUCT2 

print("VALOR A PAGAR: R$ %0.2f" % TOTAL)
