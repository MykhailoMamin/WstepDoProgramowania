#Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
#oraz wyświetla wyniki na ekranie.

x=float(input("Podaj długośc boku A: "))
y=float(input("Podaj długośc boku B: "))
obwod=((2*x)+(2*y))
pole=x*y
print(f"Obwod: {obwod}")
print(f"Pole: {pole}")