x = input("Greeting: ")
x = x.strip().casefold()

if x.startswith("hello"):
    print("$0", end="")
elif x.startswith("h"):
    print("$20", end="")
else:
    print("$100", end="")
