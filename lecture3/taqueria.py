sum = 0
sum = float(sum)

menu = {
      "Baja Taco": 4.25,
      "Burrito": 7.50,
      "Bowl": 8.50,
      "Nachos": 11.00,
      "Quesadilla": 8.50,
      "Super Burrito": 8.50,
      "Super Quesadilla": 9.50,
      "Taco": 3.00,
      "Tortilla Salad": 8.00
}

while True:
      try:
                item = input("Item: ").title()
                sum += menu[item]
                sum = round(sum, 2)
                print(f"Total: ${sum:.2f} ")

      except ValueError:
                continue

      except NameError:
                continue

      except KeyError:
                continue

      except EOFError:
                break
