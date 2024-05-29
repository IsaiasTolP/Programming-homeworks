#!/bin/bash

####################################
#
# Nombre: ej14-pares.sh
# Autor: Isaías
#
# Objetivo: El cuadrado de los números pares entre 2 números
#
# Entradas: 2 números
# Salidas: Cuadrado de los números pares entre ambos números.
#
# Historial:
#        2024-01-26: Versión 1
#
####################################

num_1="$1"
num_2="$2"

while [ -z "$num_1" ] && [ -z "$num_2" ]
do
    read -p "Introduzca un número: " num_1
    read -p "Introduzca otro número: " num_2
done

if [ "$num_1" -gt "$num_2" ] ; then
    bigger_num="$num_1"
    lower_num="$num_2"
else
    bigger_num="$num_2"
    lower_num="$num_1"   
fi

bigger_num=$(( bigger_num - 1 ))
lower_num=$(( lower_num - 1 ))

for num in `seq $bigger_num -1 $lower_num`
do
    remainder=$(( num % 2 ))
    if [ "$remainder" -eq 0 ] ; then
        echo "El cuadrado del número par $num es $(( num**2 ))"
    fi
done
