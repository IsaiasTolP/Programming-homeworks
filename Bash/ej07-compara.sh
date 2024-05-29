#!/bin/bash

######################################
#
# Nombre: ej07-compara.sh
# Autor: Isaías
#
# Objetivo: Comparar 2 números
#
# Entradas: 2 Números
# Salidas: Cual es mayor o si son iguales
#
# Historial:
#       2024-01-09: versión 1
#
#####################################

value_1="$1"
value_2="$2"

if [ "$#" -eq 0 ] ; then
  echo "Usted debe introducir 2 valores numéricos"
  echo "Por favor revise la SINTAXIS: $0 <valor1> <valor2>"
  read -p "Introduzca el primer valor: " value_1
  read -p "Introduzca el segundo valor: " value_2
elif [ -z "$value_2" ] ; then
  echo "Tiene que introducir un segundo valor, por favor indiquelo a continuación"
  read -p "aquí: " value_2
elif [ -z "$value_1" ] ; then
  echo "No ha introducido el primer valor, por favor indíquelo a continuación"
  read -p "Aquí: " value_1
fi
if [ "$value_1" -eq "$value_2" ] ; then
  echo "Los dos valores introducidos son iguales"
elif [ "$value_1" -gt "$value_2" ] ; then
  echo "El $value_1 es mayor que el $value_2"
else
  echo "El $value_2 es mayor que el $value_1"
fi
