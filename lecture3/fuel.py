while True:
      x = input("Fraction: ")

    if x == "F" or x == "100/100" or x == "99/100":
              print("F")
              break

elif x == "E" or x == "1/100" or x == "0/100":
          print("E")
          break

else:
          try:
                        first_int, second_int = x.split("/")
                        first_int = int(first_int)
                        second_int = int(second_int)

              if first_int < 0:
                                continue

            if first_int > second_int:
                              continue

            break

except ValueError:
            continue

except ZeroDivisionError:
            continue

output = (first_int / second_int) * 100
output = round(output)
print(str(output)+"%")
