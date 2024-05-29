#!/bin/bash

####################################
#
# Nombre: bucle_cuadrado.sh
# Autor: Isaías
#
# Objetivo: Ejemplos simples de bucles
#
# Entradas: Valor máximo
# Salidas: Todos los resultados de una potencia cuadrada desde el 0 al máximo
#
# Historial:
#        2024-01-15: Versión 1
#        2024-01-15: Versión 2, con límite      
#
####################################

for value in {1..100}
do
    echo "El cuadrado de $value es: $(( $value**2 ))"
done

read -p "Indique un valor máximo :" n

for value in `seq 0 $n`
do
    echo "El cuadrado de $value es: $(( $value**2 ))"
done