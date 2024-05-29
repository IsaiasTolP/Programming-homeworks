#!/bin/bash

####################################
#
# Nombre: ej20-calculadora-func.sh
# Autor: Isaías
#
# Objetivo: Calculadora usando funciones
#
# Entradas: 2 valores
# Salidas: El resultado de las operaciones
#
# Historial:
#        2024-01-28: Versión 1
#        
####################################

val_1="$1"
val_2="$2"

if [ $# -ne 2 ] ; then
    echo "ERROR, debe indicar DOS valores"
    echo "SINTAXIS: $0 <valor1> <valor2>"
    exit
fi

suma() {
    local sum_res=$(( $1 + $2 ))
    echo "$sum_res"
}

resta() {
    local substr_res=$(( $1 - $2 ))
    echo "$substr_res"
}

multip() {
    local mul_res=$(( $1 * $2 ))
    echo "$mul_res"
}

division() {
    local div_res=$(( $1 / $2 ))
    echo "$div_res"
}

resto() {
    local remain_res=$(( $1 % $2 ))
    echo "$remain_res"
}

potencia() {
    local power_res=$(( $1 ** $2 ))
    echo "$power_res"
}

echo "Tenga en cuenta que las divisiones no pueden dar numeros decimales, ya que no están soportados en Shell"
PS3="Elija una de las opciones: "
select option in "Sumar" "Restar" "Multiplicar" "Dividir" "Resto" "Elevar" "Salir"
do

    case $option in

        "Sumar") echo "El resultado de $val_1 + $val_2 = $(suma $val_1 $val_2)" ;;
        "Restar") echo "El resultado de $val_1 - $val_2 = $(resta $val_1 $val_2)" ;;
        "Multiplicar") echo "El resultado de $val_1 * $val_2 = $(multip $val_1 $val_2)" ;;
        "Dividir") echo "El resultado de $val_1 / $val_2 = $(division $val_1 $val_2)" ;;
        "Resto") echo "El resto de $val_1 / $val_2 = $(resto $val_1 $val_2)" ;;
        "Elevar") echo "El resultado de $val_1 ^ $val_2 = $(potencia $val_1 $val_2)" ;;
        "Salir") break ;;
        *) echo "ERROR, ha indicado una opción incorrecta"
    esac

done
