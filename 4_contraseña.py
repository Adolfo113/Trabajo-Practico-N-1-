import re  

regex = re.compile(r"(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z].*[a-z])(?=.*\W).{8,}")


passw= input('Ingrese una contraseña:')


if regex.match(passw):
        print(f'La contraseña {passw} fue creada exitosamente')
        
else:
        print(f'Contraseña {passw} no valida, debe contener al menos 8 caracteres, una mayuscula, un numero y un caracter especial')
        