#!/bin/bash

######################################
#
# Nombre: ej02-crea_usuario.sh
# Autor: Isaías
#
# Objetivo: hacer pequeñas pruebas con script
#
# Entradas: Ninguna se piden por teclado
# Salidas: Mensaje de bienvenida
#
# Historial:
#       2024-01-8: versión 1.
#       2024-01-15: Versión 2, entradas por teclado.
#
#####################################

sleep 15

read -p "Indique su nombre: " name
read -p "Indique su apellido: " surname
read -p "Indique su usuario: " username

echo "Bienvenido $name"
echo "Tus datos son: $name $surname"
echo "Tu usuario es: $username"
echo "Vamos a crear tu ID: $RANDOM"
