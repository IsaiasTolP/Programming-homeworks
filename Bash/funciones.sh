#!/bin/bash

####################################
#
# Nombre: funciones.sh
# Autor: Isaías
#
# Objetivo: Ejemplos basicos de funciones
#
# Entradas: No
# Salidas: No
#
# Historial:
#        2024-01-19: Versión 1
#        
####################################

# Definir una función
# Modo 1
function media2v {
    local a=$1 # Dentro de las funciones es ideal poner local, ya que en bash las variables de dentro de las funciones se pueden confundir con las de fuera.
    local b=$2

    if [ -z "$a" ] || [ -z "$b" ] ; then
        return $ERR_NOARG
    fi
    local med=$(( (a+b)/2 ))
    echo "$med"
    return 0
} 
# Hay que evitar mostar mensajes dentro de una función (Como errores y demás)
# Por supuesto no deberíamos usar un exit, porque se saldría del programa, por ejemplo el return (que solo aborta la función).

# Modo 2
mediaNv() {

    if [ $# -eq 0 ] ; then
        return $ERR_NOARG
    fi

    local sum=0
    for value in "$@"
    do
        (( sum += value ))
    done
    medi=$(( sum/$# ))
    echo "$medi"
}

# Modo 3
function mediaMv() {
    
    local sum=0
    local num_arg=0
    while [ -n $1 ]
    do
        (( sum+=$1 ))
        (( num_arg++ ))
        shift
    done
    echo "$(( sum/num_arg ))"
}

res=$(media2v 4 7)
echo "El resultado es $res"
echo "El error devuelto es $?" # Este siempre dará bien porque el está dando el error del echo que está bien.
echo "El error devuelto es $cod_err"

media2v
echo "El error devuelto es $?" # Este da mal, si la función da mal, ya que está devolviendo el error de la misma.
