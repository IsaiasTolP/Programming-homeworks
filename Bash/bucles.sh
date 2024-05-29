#!/bin/bash

####################################
#
# Nombre: bucles.sh
# Autor: Isaías
#
# Objetivo: Ejemplos simples de bucles
#
# Entradas: No
# Salidas: Algo
#
# Historial:
#        2024-01-15: Versión 1        
#
####################################

for i in 1 2 3 4 5 6 7 8 9 10 # Un for que recorre los 10 números.
do
    echo "El valor de i es $i"
done

for i in "Monaco" "Francia" "Reino Unido" "Italia" # Un for que recorre los 4 países
do
    echo "El país es $i"
done

for i in {1..20..3} # Un Range que va del 1 al 20 de 3 en 3.
do
    echo "El valor de i es $i"
done

for i in {20..1} # Un Range decreciente del 20 al 1
do
    echo "El valor de i es $i"
done
