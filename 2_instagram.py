import re

re = re.compile(r'^@(\w){1,30}$')

while True:
    cuenta = (input("Ingrese su usuario de Instagram: "))
    letras = len(cuenta)
    if re.match(cuenta):
        print("Su usuario es válido")
        break
    if (letras < 2 or letras > 31):
        print("Su usuario debe contener entre 1 y 30 caracteres . Intente nuevamente") 
    else:
        print("Su usuario no es válido. Intente nuevamente")
