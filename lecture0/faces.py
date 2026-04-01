def main():
    y = input("")
    print(convert(y))


def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x


main()
