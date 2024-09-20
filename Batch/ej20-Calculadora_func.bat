@echo off

title Calculadora funciones
REM *********************************
REM * Nombre: ej20-Calculadora_func.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Una Calculadora funcional que use funciones.
REM * 
REM * Entrada: 2 valores.
REM * Salida: El resultado de la operación seleccionada.
REM *
REM *********************************

set a=%1
set b=%2

if "%a%" == "" (
	set /p a=Introduzca el primer dato:
)
if NOT DEFINED b (
	set /p b=Introduzca el segundo dato:
)

cls
echo.
echo ***********
echo * M E N U *
echo ***********
echo.
echo Los datos son a=%a% y b=%b%
echo.
echo 1. Sumar
echo 2. Restar
echo 3. Multiplicar
echo 4. Dividir
echo 5. Modulo

choice /C 12345 /M "Elige entre una de las opciones "

if %errorlevel% EQU 1 call :sumar %a% %b%
if %errorlevel% EQU 2 call :restar %a% %b%
if %errorlevel% EQU 3 call :multiplicar %a% %b%
if %errorlevel% EQU 4 call :dividir %a% %b%
if %errorlevel% EQU 5 call :modulo %a% %b%

exit /b 0 
REM Hay que indicar donde acaba el programa principal y las funiciones

:sumar
	set /a res=%1 + %2
	echo El resultado de la suma es %res%
	exit /b 0
	
:restar
	set /a res=%1 - %2
	echo El resultado de la resta es %res%
	exit /b 0
	
:multiplicar
	set /a res=%1 * %2
	echo El resultado de multiplicar es %res%
	exit /b 0

:dividir
	set /a res=%1 / %2
	echo El resultado de dividir es %res%
	exit /b 0

:modulo
	set /a res=%1 %% %2
	echo El resultado del modulo es %res%
	exit /b 0