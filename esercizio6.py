def radici(a,b,c):
    delta = ((b*b)-(4*a*c))
    x1 = ((-b)-delta)//2*a
    x2 = ((-b)+delta)//2*a
    return f"Le due radici dell'equazione sono: {x1} e {x2}"

a = int(input("Coefficiente a: "))
b = int(input("Coefficiente b: "))
c = int(input("Coefficiente c: "))
print(radici(a,b,c))
