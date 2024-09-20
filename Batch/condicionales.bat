@echo off

REM *********************************

REM Comprobar si una variable está definida
if defined var (
	echo var esta definida y vale %var%
)	else (
	echo var NO esta definida
)

REM NEGAR una condicion
if NOT defined a echo La variable a NO esta definida

set a=hola
REM COMPARAR TEXTOS
if "%a%" == "Hola" (
	echo La variable a dice Hola
)	else (
	echo La variable a dice otra cosa: %a%
)
REM Mas ayuda: help if

set /p disco=Dime un elemento del disco (fichero, directorio, etc)
if EXIST %disco% (
	echo CORRECTO!! %disco% SI existe
	echo.
	dir %disco%
)	else (
	echo Lo siento, %disco% NO existe
)

REM COMPARA NUMEROS
REM PYTHON | BASH | BAT
REM    ==  | -eq  | equ
REM    !=  | -ne  | neq
REM    >   | -gt  | gtr
REM    >=  | -ge  | geq
REM    <   | -lt  | lss
REM    <=  | -le  | leq

set /p edad=Dime tu edad:
if %edad% lss 18 (
	echo Lo siento, eres MENOR de edad
)	else (
	echo Felicidades, eres MAYOR de edad
)

REM No hay "AND" ni "OR"
if cond1 if cond2 if cond3 (
...
)

set res=F
if cond1 res=T
if cond2 res=T
if cond3 res=T

if "%res%" == "T" (
...
)
