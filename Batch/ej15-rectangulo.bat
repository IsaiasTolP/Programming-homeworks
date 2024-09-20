@echo off

title calcula rectangulo

REM **************************************
REM * Nombre: ej15-rectangulo.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Creador de rectángulos
REM *
REM * Entrada: Numero de columnas, número de filas
REM * Salida: Un rectángulo con el número indicado de filas y columnas
REM *
REM ***************************************

setlocal enabledelayedexpansion

set base=%1
set heigth=%2

if NOT defined base (
    set base=7
    echo No se ha indicado base usaremos 7
)
if NOT defined heigth (
    set heigth=4
    echo No se ha indicado altura usaremos 4
)

set /a area=%base% * %heigth%

echo Vamos a pintar un rectangulo con base %base% y altura %heigth%, de area %area%
for /L %%i in (1 1 !heigth!) do (
    for /L %%k in (1 1 !base!) do (
        set /p =# <nul
    )
    echo. 
)

endlocal