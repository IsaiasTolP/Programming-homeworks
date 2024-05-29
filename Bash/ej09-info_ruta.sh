#!/bin/bash

######################################
#
# Nombre: ej09-info_ruta.sh
# Autor: Isaías
#
# Objetivo: Comprobar si algo existe en el disco y que tipo de archivo es.
#
# Entradas: 1 argumento cualquiera.
# Salidas: Existencia en el disco y su tipología.
#
# Historial:
#       2024-01-23: versión 1
#
#####################################

name="$1"

while [ -z "$name" ]
do 
    echo "Usted no ha introducido algo que corroborar"
    read -p "Indíquelo a continuación: " name
done

if [ -n "$name" ] ; then
    echo "Su archivo existe"
else
    echo "ERROR: este archivo no existe"
    exit
fi

if [ -f "$name" ] ; then
    echo "'$name' es un fichero"
elif [ -d "$name" ] ; then
    echo "'$name', es un directorio"
elif [ -h "$name" ] ; then
    echo "'$name', es un enlace"
else
    echo "'$name' es de un tipo especial"
fi

if [ -r "$name" ] ; then
    echo "'$name' tiene permiso de lectura"
else
    echo "'$name' no tiene permiso de lectura"
fi
if [ -w "$name" ] ; then
    echo "'$name' tiene permiso de escritura"
else
    echo "'$name' no tiene permiso de escritura"
fi
if [ -x "$name" ] ; then
    echo "'$name' tiene permiso de ejecución/acceso"
else
    echo "'$name' no tiene permiso de ejecución/acceso"
fi

if [ -s "$name" ] ; then
    echo "Este archivo no está vacío"
else
    echo "Este archivo está vacío"
fi

