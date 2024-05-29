#!/bin/bash

###############################
#
# Nombre: ej05-calcula_segundos.sh
# Autor: Isaías
#
# Objetivo: Obtener los segundos que son una serie de días, horas, minutos y segundos
#
# Entradas: Días, horas, minutos y segundos
# Salidas: Segundos
#
# Historial:
#        2024-01-11: Versión 1
#
################################

days="$1"
hours="$2"
minutes="$3"
seconds="$4"

days_in_second="$(($days*24*3600))"
hours_in_second="$(($hours*3600))"
minutes_in_second="$(($minutes*60))"
total_seconds="$(($days_in_second+$hours_in_second+$minutes_in_second+$seconds))"

echo "Sus $days días, $hours horas, $minutes minutos y $seconds segundos son $total_seconds segundos"
