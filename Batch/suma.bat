@echo off

title A sumar

REM ****************************
REM * Nombre: suma.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: sumar dos valores
REM *
REM ****************************

set /a a = 56
set /a b = 12

set /a resultado = %a% + %b%

echo La suma de %a% + %b% = %resultado%