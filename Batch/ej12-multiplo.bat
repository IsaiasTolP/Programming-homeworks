@echo off

title multiplos

REM *********************************
REM * Nombre: ej12-multiplo.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Una Calculadora de multiplos de un número.
REM * 
REM * Entrada: Los valores que se deseen comparar y un comparador por teclado.
REM * Salida: Cual número es múltiplo y cual no.
REM *
REM *********************************

setlocal enabledelayedexpansion

set /p to_compare=Introduzca el numero con el que desea calcurar los multiplos:

for %%m in (%*) do (
    set /a res=%%m %% !to_compare!

    if !res! EQU 0 (
        echo el %%m es multiplo de !to_compare!
    ) else (
        echo el %%m no es multiplo de !to_compare!
    )
)

endlocal
