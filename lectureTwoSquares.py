def main():
    n = int(input("Please input a number:\n"))
    increment = 0

    for i in range(0, n):
        square = i*i

        if increment > 0:
            print(i, i * i)

        increment=increment+1


main()
