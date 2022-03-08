
def grade():
    print("This program will determine your grade based on your %.")

    score = int(input("Please enter your mark as a %: \n"))
    if score > 90:
        print("A")
    elif score > 80:
        print("B")
    elif score > 70:
        print("C")
    elif score > 60:
        print("D")
    elif score < 60:
        print("You suck moron!")




grade()