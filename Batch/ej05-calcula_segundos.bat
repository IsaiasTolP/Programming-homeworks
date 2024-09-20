@echo off

title calcula segundos

REM **************************************
REM * Nombre: ej05-calcula_segundos.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Calcular la equivalencia en segundos.
REM *
REM * Entrada: días, horas, minutos y segundos (en ese orden).
REM * Salida: Número de segundos.
REM *
REM ***************************************

set days=%1
set hours=%2
set mins=%3
set secs=%4

set /a days_in_secs= %days% * 86400
set /a hours_in_secs= %hours% * 3600
set /a mins_in_secs= %mins% * 60
set /a result= %days_in_secs% + %hours_in_secs% + %mins_in_secs% + %secs%

echo El resultado de sus %days% dias, %hours% horas, %mins% minutos y %secs% segundos en segundos es de %result%