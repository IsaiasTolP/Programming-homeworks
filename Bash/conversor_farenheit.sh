#!/bin/bash

######################################
#
# Nombre: conversor_farenheit.sh
# Autor: Isaías
#
# Objetivo: Convertir Farenheit a Celsius
#
# Entradas: grados Farenheit
# Salidas: grados Celsius
#
# Historial:
#       2023-12-18: versión 1
#
#####################################


result="$((($1-32)*5/9))"

echo "Son $result Celsius"
