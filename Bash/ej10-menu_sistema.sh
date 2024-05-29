#!/bin/bash

####################################
#
# Nombre: ej10-menu_sistema.sh
# Autor: Isaías
#
# Objetivo: Crear un Menú con funcionalidades que aporten información sobre el sistema.
#
# Entradas: El número de la acción que se quiera realizar (por teclado)
# Salidas: La salida correspondiente a la opción
#
# Historial:
#        2024-01-23: Versión 1
#
###################################

clear
echo "*************"
echo "** M E N U **"
echo "*************"
echo ""
echo "1/porlibre: Mostrar porcentaje de disco usado."
echo "2/tamlibre: Mostrar espacio libre del disco."
echo "3/usuario: Mostrar tu usuario."
echo "4/maquina: Mostrar nombre de la máquina."
echo "5/usuarios: Mostrar los usuarios del sistema."
echo "6/espacio: Espacio usado en los directorios personales."
echo "7/memoria: Muestra la memoria libre"
echo "8/ejecucion: Da permisos de ejecución a todos los scripts de bash"
echo ""
read -p "Introduzca su opción: " option

case "$option" in
    porlibre|1) df / -h | tr -s " " | cut -d " " -f 5
    ;;

    tamlibre|2) df / -h | tr -s " " | cut -d " " -f 4
    ;;

    usuario|3) whoami
    ;;

    maquina|4) uname -n
    ;;

    usuarios|5) compgen -u | wc -l
    ;;

    espacio|6) df -h /run/user/1000 | tr -s " " | cut -d " " -f 4
    ;;

    memoria|7) free -h
    ;;

    ejecucion|8) chmod u+x *.sh
    ;;

    *) echo "ERROR, esa opción no es válida"
    ;;

esac
