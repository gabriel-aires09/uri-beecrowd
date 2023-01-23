import math

lineOne = input().split(" ")
lineTwo = input().split(" ")

x1, y1 = lineOne
x2, y2 = lineTwo

split = lineOne
x1 = float(split[0])
y1 = float(split[1])

split = lineTwo
x2 = float(split[0])
y2 = float(split[1])

result = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
square = math.sqrt(result)

print("%0.4f" % square)
