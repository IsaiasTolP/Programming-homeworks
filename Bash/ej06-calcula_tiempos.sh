#!/bin/bash

###############################
#
# Nombre: ej06-calcula_tiempos.sh
# Autor: Isaías
#
# Objetivo: Obtener los días, horas, minutos y segundos que son unos segundos
#
# Entradas: Segundos
# Salidas: Días, horas, minutos y segundos
#
# Historial:
#        2024-01-11: Versión 1
#
################################

seconds="$1"

days="$(($seconds/(3600*24)))"
seconds_remain="$(($seconds%(3600*24)))"
hours="$(($seconds_remain/3600))"
seconds_remain="$(($seconds_remain%3600))"
minutes="$(($seconds_remain/60))"
seconds_remain="$(($seconds_remain%60))"

echo "Sus $seconds segundos son $days días, $hours horas, $minutes minutos y $seconds_remain segundos"
