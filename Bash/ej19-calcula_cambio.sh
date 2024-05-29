#!/bin/bash

####################################
#
# Nombre: ej19-calcula_cambio.sh
# Autor: Isaías
#
# Objetivo: Calcular el cambio de dinero que se debe devolver
#
# Entradas: El dinero a pagar y el dinero que se recibe
# Salidas: El cambio a devolver
#
# Historial:
#        2024-01-21: Versión 1
#
####################################

read -p "Indique cuanto ha pagado: " money
price="$1"
to_return="$((money-price))"
copy_return="$to_return"

declare -A final_change

available_change=(500 200 100 50 20 10 5 2 1)

for change in "${available_change[@]}"
do
    if [ "$change" -le "$copy_return" ] ; then
        final_change[$change]=0
        count=0
    fi
    while [ "$change" -le "$copy_return" ]
    do
        (( count++ ))
        final_change[$change]="$count"
        copy_return="$(( $copy_return - $change ))"
    done
done

echo "Se ha comprado un artículo de $price€ y ha pagado $money€."

echo "El cambio son $to_return€, debe entregar:"
for key in "${!final_change[@]}"
do
    echo "${final_change[$key]} billete(s) de $key."
done