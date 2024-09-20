@echo off

title suma argumenta

REM ****************************
REM * Nombre: suma_arg.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: sumar dos valores indicando argumentos
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

set /a resultado = %a% + %b%

echo La suma de %a% + %b% = %resultado%
REM El echo. imprime una linea en blanco
echo.