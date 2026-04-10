name = input("camelCase: ")

result = ""

for l in range(len(name)):
    if name[l].isupper():
        result += "_" + name[l].lower()
    else:
        result += name[l]

print(result)
