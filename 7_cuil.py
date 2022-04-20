import re 

regex = re.compile(r"^\b(20|23|24|27|30|33|34)(\D)?[0-9]{8}(\D)?[0-9]$")

while True:
    cuil= input("\nIngrese su CUIL: ")
    if regex.match(cuil):
        print("CUIL VALIDO")
        break
    print('El CUIL es invalido')
