a = 5
b = 0


try:
    print(a / b)
except NameError:
    print("Hej nie ma takiej zmiennej")
except ZeroDivisionError:
    print("Nie mozna dzielic przez zero")
else:
    print("ok")
finally:
    print("zawsze")

print("koniec")
