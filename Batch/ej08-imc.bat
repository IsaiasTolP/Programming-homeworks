@echo off

title calcula imc

REM **************************************
REM * Nombre: ej08-imc.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Calculador de índice de masa corporal
REM *
REM * Entrada: Altura(cm) y peso(Kg)
REM * Salida: Índice de masa corporal (IMC)
REM *
REM ***************************************

set heigth=%1
set weigth=%2

if NOT defined heigth (
    echo Usted no ha introducido los valores de forma correcta
    echo Recuerde la sintaxis es: %0 [altura_en_cm] [peso_en_Kg]
    exit /b 1
)
if NOT defined weigth (
    echo Usted no ha introducido los valores de forma correcta
    echo Recuerde la sintaxis es: %0 [altura_en_cm] [peso_en_Kg]
    exit /b 1
)

set /a imc=(10000 * %weigth%) / (%heigth% * %heigth%)

if %imc% lss 16 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una delgadez severa.
) else if %imc% lss 17 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una delgadez moderada.
) else if %imc% lss 19 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una delgadez leve.
) else if %imc% lss 25 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone unos valores normales.
) else if %imc% lss 30 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una preobesidad.
) else if %imc% lss 35 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una obesidad leve.
) else if %imc% lss 40 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una obesidad media.
) 
if %imc% geq 40 (
    echo Su Indice de Masa Corporal es de %imc%, esto supone una obesidad mórbida.
)

echo Tenga en cuenta que este es un programa que solo tiene en cuenta operaciones muy básicas, si quiere mejor información acuda a un profesional
