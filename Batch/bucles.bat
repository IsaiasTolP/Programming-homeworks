@echo off

REM *********************************

REM Variables de iteración en los bucles for en batch
REM 1) Una única letra - CASE SENSITIVE
REM 2) En la línea de comandos se usa %i, pero en script se debe usar %%i

REM Bucle simple indicando valores (se pueden separar por comas y/o espacios)
for %%i in (1, 56,	765 34 23 56) do (
	echo Los valores son %%i
)
echo.
pause
REM bucle por rango
REM 	      ini  step  end
for /L %%i in (1    2    21) do (
	echo Los valores con rango son %%i
)
echo.
pause

echo Iterar por fichero:
REM Debo indicar el nombre del fichero o los COMUNES: *, *.???, a*.cmd, etc
for %%f in (*.???) do (
	echo Los fichero son %%f
)
echo.
pause

REM Iterar por directorios
for /D %%d in (*) do (
	echo Los directorios son %%d
)
echo.
pause

REM Iterar de forma recursiva
for /R %%e in (*) do (
	echo Los elementos son %%e
)
echo.

REM La opción /F funciona con tokens y delimitadores (similar al cut de bash)