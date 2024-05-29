#!/bin/bash

######################################
#
# Nombre: script.sh
# Autor: Isaías
#
# Objetivo: hacer pequeñas pruebas con script
#
# Entradas: ninguna
# Salidas: ninguna
#
# Historial:
#	2023-12-18: versión 1
#
#####################################

ls -la | grep rwx | cut -d "-" -f 2 | wc -c
