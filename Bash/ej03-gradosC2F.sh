#!/bin/bash

######################################
#
# Nombre: conversor_farenheit.sh
# Autor: Isaías
#
# Objetivo: Convertir Farenheit a Celsius
#
# Entradas: grados Celsius
# Salidas: grados Fahrenheit
#
# Historial:
#       2024-01-09: versión 1
#       2024-01-09: versión 2 con un input
#
#####################################

celsius="$1"

echo "Los argumentos que has indicado son: $*" #Lo devuelve en cadena de texto
echo "Los argumentos que has indicado son: $@" #Lo devuelve en un array
echo "Estoy en la línea $LINENO, llevo ejecutando $SECONDS y fui ejecutado por $USER" #Tal como lo describe el texto

if [ $# -eq 0 ] ; then
   echo "ERROR: No has indicado argumentos. Debes indicar 1 argumento, con el dato de grados Celsius"
   echo "SINTAXIS: $0 <grados Fahrenheit>"
   exit
elif [ $# -ge 2 ] ; then
   echo "Este script solo acepta un argumento, vea la sintaxis debajo"
   echo "SINTAXIS: $0 <grados Fahrenheit>"
   exit
else
   echo "Has indicado $# argumentos"
fi

fahrenheit=$(bc <<< "$celsius*1.8+32")
echo "La temperatura es de $fahrenheit Fº"
