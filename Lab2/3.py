s = '''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie'''
print(s)
operation = input("Wpisz numer operacji: ")
x = float(input("Podaj argument 1: "))
y = float(input("Podaj argument 2: "))


if operation ==1:
    z =(f"{x}+{y}={x+y}")
elif operation ==2:
    z = (f"{x}-{y}={x - y}")
elif operation ==3:
    z = (f"{x}/{y}={x/y}")
elif operation ==4:
    z = (f"{x}*{y}={x * y}")
elif operation ==5:
    z = (f"{x}**{y}={x ** y}")
else:
    print("Error")
print(z)
