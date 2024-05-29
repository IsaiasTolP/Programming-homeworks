#!/bin/bash

####################################
#
# Nombre: menu_case.sh
# Autor: Isaías
#
# Objetivo: Crear un Menú con funcionalidades de la terminal usando case
#
# Entradas: Las entradas propuestas
# Salidas: La salida correspondiente
#
# Historial:
#        2024-01-12: Versión 1
#
###################################

clear
echo "*************"
echo "** M E N U **"
echo "*************"
echo ""
echo "a: Mostrar el contenido del directorio"
echo "b: Mostrar el espacio libre del disco"
echo "c: Mostrar los permisos del contenido"
echo "d: Mostrar la memoria libre"
echo ""
read -p "Introduzca su opción: " option

case "$option" in
    a|A|1) ls -lh
    ;;

    b|B|2) df -h
    ;;

    c|C|3) stat -c "%a %A %n" *
    ;;

    d|D|4) free
    ;;

    *) echo "ERROR: '$option' no es una opción correcta"
    ;;

esac
