#!/bin/bash

####################################
#
# Nombre: ej08-imc.sh
# Autor: Isaías
#
# Objetivo: Calculador de índice de masa corporal
#
# Entradas: Altura(cm) y peso(Kg)
# Salidas: Índice de masa corporal (IMC)
#
# Historial:
#        2024-01-14: Versión 1
#        2024-01-14: Versión 2, ahora con 2 decimales.
#
####################################

height="$1"
weight="$2"
decimals=2

if [ $# -ge 0 ] && [ $# -lt 2 ] || [ $# -gt 2 ] ; then
    echo "Usted no ha introducido los valores de forma correcta"
    echo "Recuerde la sintaxis es: $0 <altura_en_cm> <peso_en_Kg>"
    exit
fi

imc=$(echo "scale=$decimals; (10000 * $weight) / ($height ^ 2)" | bc)

if (( $(echo "$imc < 16" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una delgadez severa."
elif (( $(echo "$imc < 17" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una delgadez moderada."
elif (( $(echo "$imc < 18.50" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una delgadez leve."
elif (( $(echo "$imc < 25" | bc -l) )) ; then # No es necesario ninguna de las comparaciones ">=", ya que ya están incluidas.
    echo "Su Índice de Masa Corporal es de $imc, esto supone unos valores normales."
elif (( $(echo "$imc < 30" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una preobesidad."
elif (( $(echo "$imc < 35" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una obesidad leve."
elif (( $(echo "$imc < 40" | bc -l) )) ; then
    echo "Su Índice de Masa Corporal es de $imc, esto supone una obesidad media."
else
    echo "Su Índice de Masa Corporal es de $imc, esto supone una obesidad mórbida."
fi

echo ""
echo "Tenga en cuenta que este es un programa que solo tiene en cuenta operaciones muy básicas, si quiere mejor información acuda a un profesional"

