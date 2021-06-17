x = "hello"
print(type(x))

if not type(x) is int:
    raise TypeError("tylko liczby są akceptowane")
