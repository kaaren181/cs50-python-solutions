months = {

    "January": 1,

    "February": 2,

    "March": 3,

    "April": 4,

    "May": 5,

    "June": 6,

    "July": 7,

    "August": 8,

    "September": 9,

    "October": 10,

    "November": 11,

    "December": 12

}




while True:

    date = input("Date: ").strip()

    if date[0].isalpha():

        try:




            x, y, z = date.split(" ")

            y = y[:-1]

            y = int(y)

            w = months[x]

            w = int(w)

            if y > 31:

                continue

            print(f"{z}-{w:02d}-{y:02d}")

            break

        except ValueError:

            continue

        except KeyError:

            continue

    try:

        if date[0].isdigit():

            a, b, c = date.split("/")

            a, b = int(a), int(b)

            if not (1 <= a <= 12 and 1 <= b <= 31):

                continue

            print(f"{c}-{a:02d}-{b:02d}")

            break

    except ValueError:

        continue
