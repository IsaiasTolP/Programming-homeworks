#!/bin/bash

######################################
#
# Nombre: ej09-info_ruta.sh
# Autor: Isaías
#
# Objetivo: Comprobar que tiene más de 4 caracteres y ejecutarle el script 09.
#
# Entradas: 1 argumento cualquiera.
# Salidas: Si tiene o no más de 4 caracteres y la salida del script 09.
#
# Historial:
#       2024-01-26: versión 1
#
#####################################

name="$1"

if [ "${#name}" -ge 5 ] ; then
    echo "Felicidades, su archivo tiene la cantidad caracteres correctos. Procederemos con la operación"
    echo ""
    ./ej09-info_ruta.sh "$name"
else
    echo "ERROR Su archivo no tiene más de 4 caracteres, no se puede llevar a cabo la operación"
fi
