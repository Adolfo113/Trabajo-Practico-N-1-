import re 

regex = re.compile(r'^\d{1,3}(\.\d{3})(,\d{2})?|\d{1,3}(,\d{2})$')


number = input("Ingrese un numero real con separador de miles y dos decimales: ")

if regex.match(number):
    print('El numero real es valido')
else:
    print('El numero real ingresado es invalido')
    