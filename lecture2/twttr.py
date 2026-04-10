start = input("Input: ")

end = ""

for l in range(len(start)):
    if start[l].lower() != "a" and start[l].lower() != "o" and start[l].lower() != "u" and start[l].lower() != "i" and start[l].lower() != "e":
        end += start[l]
    else:
        None

print(end)
