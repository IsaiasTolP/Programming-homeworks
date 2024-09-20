@echo off

title resta argumental

REM ****************************
REM * Nombre: ej01-resta.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: restar dos valores indicando argumentos.
REM *
REM * Entrada: 2 valores.
REM * Salida: Resultado de la resta de ambos valores.
REM *
REM ****************************

set a=%1
set b=%2

set NO_ARG 5

if NOT defined a (
	echo ERROR!! Deberias haber indicado DOS variables
	REM exit: Finaliza el script y también la terminal donde se ejecuta
	REM si no quiero finalizar la terminal debp usar /b
	exit /b %NO_ARG%
)

if "%b%" == "" (
	echo ERROR!! Debe indicar el parametro b:
	set /p b=Indique el parametro b:
)

set /a resultado = %a% - %b%

echo La suma de %a% - %b% = %resultado%
REM El echo. imprime una linea en blanco
echo.