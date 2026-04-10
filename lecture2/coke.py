amount_d = 50

print(f"Amount Due: {amount_d}")

while True:
    x = int(input("Insert Coin: "))

    if x != 25 and x != 10 and x != 5:
        print(f"Amount Due: {amount_d}")
    else:
        amount_d -= x
        print(f"Amount Due: {amount_d}")

    if amount_d <= 0:
        amount_d *= -1
        print(f"Change Owed: {amount_d}")
        break
