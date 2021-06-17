try:
    x = int(input("podaj liczbę"))
except ValueError:
    print("musisz podac liczbe")


x = -1

if x < 0:
    raise Exception("Tylko liczby większe od zera")
