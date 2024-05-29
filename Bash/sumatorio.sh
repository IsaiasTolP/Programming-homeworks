#!/bin/bash

####################################
#
# Nombre: sumatorio.sh
# Autor: Isaías
#
# Objetivo: Ejecutar una suma de tantos valores como se indiquen
#
# Entradas: X número de valores
# Salidas: La suma de los valores
#
# Historial:
#        2024-01-16: Versión 1        
#
####################################

result=0

for value in "$@"
do
    (( result+=value ))
done

echo "El resultado de su suma es de $result"