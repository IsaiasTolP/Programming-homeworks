@echo off

title calcula cambio

REM **************************************
REM * Nombre: ej19-calcula_cambio.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Calcular el cambio de dinero que se debe devolver
REM *
REM * Entrada: El dinero a pagar y el dinero que se recibe
REM * Salida: El cambio a devolver
REM *
REM ***************************************

setlocal enabledelayedexpansion

set /p money=Indique cuanto ha pagado: 
set price=%1
set /a to_return=%money% - %price%

set available_change=500 200 100 50 20 10 5 2 1
set final_change=0

echo Se ha comprado un articulo de %price% euro(s) y ha pagado %money% euro(s).
echo El cambio son %to_return% euro(s), debe entregar:

for %%c in (%available_change%) do (
    set count=0
    call :while %%c
    if !count! NEQ 0 (
        echo !count! billete^(s^) de %%c euro^(s^).
    )
)

:end
endlocal

REM * ¿Por qué LEQ no está soportado dentro del "for" en BATCH pero NEQ sí? ¯\_(ツ)_/¯
:while
if %1 LEQ !to_return! (
    set /a count+= 1
    set /a to_return-=%1
    call :while %1
)