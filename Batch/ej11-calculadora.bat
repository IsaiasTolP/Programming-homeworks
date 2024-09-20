@echo off

REM *********************************
REM * Nombre: ej11-Calculadora.bat
REM * Autor: Isaías
REM *
REM * Objetivo: Una Calculadora funcional que realice operaciones básicas.
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

if %errorlevel% EQU 1 set /a resultado = %a% + %b%
if %errorlevel% EQU 2 set /a resultado = %a% - %b%
if %errorlevel% EQU 3 set /a resultado = %a% * %b%
if %errorlevel% EQU 4 set /a resultado = %a% / %b%
if %errorlevel% EQU 5 set /a resultado = %a% %% %b%
echo %resultado%

exit /b 0

