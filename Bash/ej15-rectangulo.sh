#!/bin/bash

####################################
#
# Nombre: ej15-rectangulo.sh
# Autor: Isaías
#
# Objetivo: Creador de rectángulos
#
# Entradas: Numero de columnas, número de filas.
# Salidas: Un rectángulo con el número indicado de filas y columnas
#
# Historial:
#        2024-01-26: Versión 1
#
####################################

if [ "$#" -eq 0 ] ; then
    echo "No ha indicado ningún argumento, vamos a usar de forma predeterminada 7 de base y 4 de altura."
    base=7
    heigth=4
elif [ "$#" -eq 1 ]; then
    echo "Usted solo ha indicado la base, usaremos una altura predeterminada de 4"
    base="$1"
    heigth=4
else
    echo "Usaremos los 2 primeros que ha introducido en orden de aparición como base y altura respectivamente"
    base="$1"
    heigth="$2"
fi

echo "Vamos a pintar un rectángulo de base: $base, altura: $heigth y área: $(( base * heigth ))"
for i in `seq 1 $heigth`
do
    for k in `seq 1 $base`
    do
        echo -n "#"
    done
    echo ""
done
