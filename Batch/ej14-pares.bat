@echo off

title pares

REM *********************************
REM * Nombre: ej14-pares.bat
REM * Autor: Isaías
REM *
REM * Objetivo: pares al cuadrado entre 2 números.
REM * 
REM * Entrada: 2 números.
REM * Salida: números pares elevados al cuadrado entre ambos.
REM *
REM *********************************

setlocal enabledelayedexpansion

set value_1=%1
set value_2=%2

:var_input
if NOT DEFINED value_1 (
    set /p value_1=Introduzca un valor 1: 
    goto var_input
)
if NOT DEFINED value_2 (
    set /p value_2=Introduzca un valor 2: 
    goto var_input
)

set /a value_1=%value_1% - 1
set /a value_2=%value_2% - 1

if %value_1% GTR %value_2% (
   for /L %%n in (!value_1! -1 !value_2!) do (
    set /a res=%%n %% 2

    if !res! EQU 0 (
        set /a pow=%%n * %%n
        echo El cuadrado del numero %%n es !pow!
    )
) 
) else (
    for /L %%n in (!value_1! 1 !value_2!) do (
     set /a res=%%n %% 2

    if !res! EQU 0 (
        set /a pow=%%n * %%n
        echo El cuadrado del numero %%n es !pow!
    )
)
)

endlocal