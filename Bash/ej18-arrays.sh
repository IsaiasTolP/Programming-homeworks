#!/bin/bash

####################################
#
# Nombre: ej18-arrays.sh
# Autor: Isaías
#
# Objetivo: 
#
# Entradas: 
# Salidas: 
#
# Historial:
#        2024-01-31: Versión 1
#
####################################

start_array=("$@")
final_array=()

echo "Se han recibido $# argumentos: $@"

for num in "${start_array[@]}"
do
if [ "$num" -lt 0 ] ; then
    echo "Se ignora el valor $num por ser negativo"
else
    module_res=$(( num%2 ))
    if [ "$module_res" -eq 0 ] ; then
        final_array=("$num" "${final_array[@]}")
        echo "$num Se inserta por el PRINCIPIO porque es PAR"
    else
        final_array+=($num)
        echo "$num Se inserta por el FINAL porque es IMPAR"
    fi
fi
done
