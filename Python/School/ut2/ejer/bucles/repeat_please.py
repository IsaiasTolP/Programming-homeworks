fullname = input('Escriba su nombre correctamente (letras con la primera mayúscula): ')

while fullname != fullname.title():
    fullname = input('Introduzca el nombre correctamente')
else:
    print('Su nombre se ha recolectado')
