@echo off

title calcula tiempo

REM **************************************
REM * Nombre: ej06-calcula_tiempos.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Calcular la equivalencia en días, horas, minutos y segundos.
REM *
REM * Entrada: segundos.
REM * Salida: días, horas, minutos y segundos (en ese orden).
REM *
REM ***************************************

set secs=%1

set /a days=%secs% / 86400
set /a secs_remain=%secs% %% 86400
set /a hours=%secs_remain% / 3600
set /a secs_remain=%secs_remain% %% 3600
set /a mins=%secs_remain% / 60
set /a secs_remain=%secs_remain% %% 60

echo Sus %secs% segundos son %days% dias, %hours% horas, %mins% minutos y %secs_remain% segundos
