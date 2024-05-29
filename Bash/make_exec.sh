#!/bin/bash

####################################
#
# Nombre: make_exec.sh
# Autor: Isaías
#
# Objetivo: Saber si un fichero tiene permiso de ejecución y si no dárselo
#
# Entradas: nombre del fichero
# Salidas: Si el permiso tiene o no permiso de ejecución. Cambiar permiso si es necesario.
#
# Historial:
#        2024-01-12: Versión 1
#
####################################

name="$1"

if [ $# -eq 0 ] ; then
    echo "Error, usted no ha introducido el nombre del fichero, se le pedíra a continuación"
    read -p "Introduzca el nombre del fichero: "
fi

if [ -f "$name" ] ; then
    if [ -x "$name" ] ; then
        echo "Su fichero '$name' tiene permisos de ejecución, NO se realizarán cambios"
    else
        echo "Su fichero no tiene permiso de ejecución, vamos a proceder a añadirlo"
        chmod +x "$name"
    fi
else
    echo "Usted no ha introducido un fichero, compruebe que lo que añade es un fichero"
fi