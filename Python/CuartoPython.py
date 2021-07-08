print("Cual es tu edad ?\t")
edad = int(input())
if edad >= 18 and edad<=59:
    print("Eres mayor de edad con:\t", edad)
elif edad>=60:
    print("Eres de la tercera edad con:\t", edad)
else:
    print("Eres menor de edad con:\t", edad)