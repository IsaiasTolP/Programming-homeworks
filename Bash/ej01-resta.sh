#!/bin/bash

####################################
#
# Nombre: ej01-resta.sh
# Autor: Isaías
#
# Objetivo: Hacer una resta entre 2 números
#
# Entradas: 2 argumentos numéricos
# Salidas: El resultado de la resta
#
# Historial:
#        2024-01-23: Versión 1
#
####################################

value_1="$1"
value_2="$2"

echo "El resultado de $1 - $2 es: $(( $1 - $2 ))"