#!/bin/bash

####################################
#
# Nombre: ej11-calculadora.sh
# Autor: Isaías
#
# Objetivo: Calculadora con 6 operaciones
#
# Entradas: 2 valores
# Salidas: El resultado de la operación seleccionada
#
# Historial:
#        2024-01-12: Versión 1
#
####################################

value_1="$1"
value_2="$2"

if [ $# -ne 2 ] ; then
    echo "ERROR, debe indicar DOS valores"
    echo "SINTAXIS: $0 <valor1> <valor2>"
    exit
fi

echo "Tenga en cuenta que las divisiones no pueden dar numeros decimales, ya que no están soportados en Shell"
PS3="Elija una de las opciones: "
select option in "Sumar" "Restar" "Multiplicar" "Dividir(Enteros)" "Resto(División)" "Elevar(Potencia)"  "Salir"
do

    case $option in

        "Sumar") echo "El resultado de $value_1 + $value_2 = $(( $value_1 + $value_2 ))" ;;
        "Restar") echo "El resultado de $value_1 - $value_2 = $(( $value_1 - $value_2 ))" ;;
        "Multiplicar") echo "El resultado de $value_1 * $value_2 = $(( $value_1 * $value_2 ))" ;;
        "Dividir(Enteros)") echo "El resultado de $value_1 / $value_2 = $(($value_1 / $value_2 ))" ;;
        "Resto(División)") echo "El resto de $value_1 / $value_2 = $(( $value_1 % $value_2 ))" ;;
        "Elevar(Potencia)") echo "El resultado de $value_1 ^ $value_2 = $(( $value_1 ** $value_2 ))" ;;
        "Salir") break ;;
        *) echo "ERROR, ha indicado una opción incorrecta"
    esac

done
