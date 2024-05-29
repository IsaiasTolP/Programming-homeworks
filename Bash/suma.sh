#!/bin/bash

######################################
#
# Nombre: script.sh
# Autor: Isaías
#
# Objetivo: hacer pequeñas pruebas con script
#
# Entradas: numeros para sumar resultado de la suma
# Salidas: resultado de la suma
#
# Historial:
#       2023-12-18: versión 1
#
#####################################

result="$(($1+$2))"

echo "$1+$2=$result"
