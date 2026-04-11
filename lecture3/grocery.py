grocery = {}

while True:

    try:

        item = input()

        grocery[item.lower()] = grocery.get(item.lower(), 0) + 1

    except EOFError:

        break




for item in sorted(grocery):

    print(grocery[item], item.upper())
