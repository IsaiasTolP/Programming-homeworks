@echo off

title compara

REM **************************************
REM * Nombre: ej07-compara.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Comparar 2 números
REM *
REM * Entrada: 2 números
REM * Salida: Cual de ellos es mayor, o decir si son iguales
REM *
REM ***************************************

set value_1=%1
set value_2=%2

if %value_1% gtr %value_2% (
    echo El valor %value_1% es mayor que el valor %value_2%
    exit /b 0
)
if %value_2% gtr %value_1% (
    echo El valor %value_2% es mayor que el valor %value_1%
    exit /b 0
)
if %value_1% equ %value_2% (
    echo Ambos valores son iguales
)

