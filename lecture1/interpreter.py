exe = input("Expression: ")
x, y, z = exe.split(" ")
x = float(x)
z = float(z)
x = round(x, 1)
z = round(z, 1)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
