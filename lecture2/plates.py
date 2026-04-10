def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number = False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    for c in s:
        if not c.isdigit() and not c.isalpha():
            return False

        if number and c.isalpha():
            return False

        if c.isdigit():
            if not number and c == "0":
                return False
            number = True

    return True
