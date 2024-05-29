#!/bin/bash

####################################
#
# Nombre: ej16-password.sh
# Autor: Isaías
#
# Objetivo: Comprobar si una contraseña es correcta
#
# Entradas: Contraseña y repetición de la misma por teclado
# Salidas: Si es correcta o no
#
# Historial:
#        2024-01-24: Versión 1
#
####################################

sleep 2
if [ "$#" -gt 0 ] ; then
    echo "No introduzca argumentos, se lo pediremos cuando sea necesario."
    exit
fi

read -s -p "Introduzca una contraseña: " password
echo ""
read -s -p "Vuelva a introducir la contraseña: " password_2
echo ""

while [ "$password" != "$password_2" ]
do
    read -s -p "ERROR: vuelva a introducir la contraseña: " password_2
done

echo ""
echo "Perfecto has introducido la contraseña correctamente 2 veces"