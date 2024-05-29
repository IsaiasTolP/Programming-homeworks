#!/bin/bash

######################################
#
# Nombre: ej04-dia_semana.sh
# Autor: Isaías
#
# Objetivo: Devolver el dia de la semana que fue.
#
# Entradas: dia, mes, año
# Salidas: dia de la semana
#
# Historial:
#       2024-01-09: versión 1
#
#####################################

day="$1"
month="$2"
year="$3"

date_format=$3-$2-$1
day_of_week=`date -d $date_format +"%A"`

echo "El dia de la semana de la semana del $1/$2/$3 fue: $day_of_week" 
