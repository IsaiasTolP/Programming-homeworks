#!/bin/bash

####################################
#
# Nombre: ej12-multiplo.sh
# Autor: Isaías
#
# Objetivo: Calculadora de múltiplos
#
# Entradas: Los que se quieran indicar
# Salidas: Si cada argumento es multiplo o no del número indicado
#
# Historial:
#        2024-01-24: Versión 1
#
####################################

args_list=("$@")
read -p "Introduzca un número para comparar " comparison
is_multiple=()

for arg in "${args_list[@]}"
do
    operation=$(( arg % comparison ))
    if [ "$operation" -ne 0 ] ; then
        is_multiple+=("No")
    else
        is_multiple+=("Sí") 
    fi
done

lenght=$(( ${#args_list[@]} - 1 ))

for index in `seq 0 $lenght`
do
    echo "El número ${comparison}, ${is_multiple[index]} es multiplo de ${args_list[index]}"
done