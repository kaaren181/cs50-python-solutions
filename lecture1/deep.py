x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x = x.casefold()
x = x.strip()
match x:
    case "42":
        print("Yes")
    case "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

