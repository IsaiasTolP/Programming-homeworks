@echo off

title usuario creacion

REM ****************************
REM * Nombre: ej03-gradosC2F.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: Convertir celsius a Fahrenheit
REM *
REM * Entrada: Grados celsius
REM * Salida: Grados Fahrenheit
REM ****************************

set celsius=%1

if "%celsius%" == "" (
	echo ERROR!! No indicaste el valor de los grados Celsius
	set /p celsius=Indique el valor de los grados Celsius: 
)

set /a Fahrenheit= ((%celsius% * 9) / 5) + 32

echo Son %Fahrenheit% Fahrenheit