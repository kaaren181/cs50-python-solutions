def main():
    meal = input("What time is it? ")
    x = convert(meal)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")




def convert(y):
    h, m = y.split(":")
    h = float(h)
    m = float(m)
    m = m / 60
    z = h + m
    return z

if __name__ == "__main__":
    main()
