@echo off

title usuario creacion

REM ****************************
REM * Nombre: ej02-crea_usuario.bat
REM * Autor: Isaias
REM * 
REM * Objetivo: Crear un usuario con sus datos e ID Random
REM *
REM * Entrada: Nombre de usuario y apellido (por teclado).
REM * Salida: Un mensaje de bienvenida.
REM *
REM ****************************

set nombre=Pepe
set /p apellido=Introduzca su apellido:
set usuario=%1
set ID=%RANDOM%

echo Bienvenido %nombre% %apellido%, su usuario es %usuario% y se le ha asignado la ID %ID%