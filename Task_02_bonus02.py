
x = input("Podaj liczbe od 1 do 100: ")
x = int(x)
how_many_numbers = 0

if x < 1:
    print("Liczba musi byc w przedziale od 1 do 100")
    quit()


if x > 100:
    print("Liczba musi byc w przedziale od 1 do 100")
    quit()

else:
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x +1

        print(x)

        how_many_numbers += 1
    print("Total number of steps: ", how_many_numbers)


