#!/bin/bash

####################################
#
# Nombre: ej17-deposito.sh
# Autor: Isaías
#
# Objetivo: Devolver el resultado del una tasa de interés compuesto
#
# Entradas: Dinero a invertir, tasa de interés, años de financiación
# Salidas: El dinero resultado por cada año
#
# Historial:
#        2024-01-26: Versión 1
#
####################################

money="$1"
rate="$2"
years="$3"
if [ "$#" -ne 3 ] ; then
    echo "ERROR, No ha indicado el número correcto de argumentos."
    exit 100
fi
initial_capital="$money"

for year in `seq 1 $years`
do
    result=$(bc <<< "scale=2; $money * (1+$rate/100)")
    benefit=$(bc <<< "scale=2; $result - $initial_capital")
    echo "Año $year: $money * (1+ $rate/100) = $result (en total has ganado $benefit)"
    money="$result"
done
