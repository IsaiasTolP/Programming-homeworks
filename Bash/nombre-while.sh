#!/bin/bash

####################################
#
# Nombre: nombre-while.sh
# Autor: Isaías
#
# Objetivo: Preguntar por un nombre hasta que se indique
#
# Entradas: Nombre
# Salidas: Su nombre
#
# Historial:
#        2024-01-16: Versión 1        
#
####################################

while [ -z "$name" ]
# until [ -n "$nombre" ]
do
    read -p "Introduzca un valor: " name
done

echo "Su nombre es $name"
