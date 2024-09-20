@echo off

title A sumar

REM ****************************
REM * Nombre: suma.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: sumar dos valores
REM *
REM ****************************

set /p a=Introduzca el primer valor:
set /p b=Introduzca el segundo valor:

set /a resultado = %a% + %b%

echo La suma de %a% + %b% = %resultado%