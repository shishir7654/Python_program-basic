try:
    a= int(input("Enter a:"))
    b = int(input("Enter b:"))

    c =a/b;
    print("a/b =%d"%c)
except Exception:
    print("cant divided by zero")
else:
    print("Hi")
