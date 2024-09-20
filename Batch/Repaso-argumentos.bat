@echo off

REM *********************************

REM %0 nombre del script
REM %1...........%9: Argumentos
REM %10, %11, %12... No se puede acceder directamente,
REM Tengo que usar "shift" para desplazar (se pierde el primer argumento, luego el segundo, etc)
REM %*: Ver todos los Argumentos
REM %1: Imprime el primer argumento "tal cual"
REM %~1: Imprime el primer argumento SIN COMILLAS

echo El script se llama %0
echo Todos los argumentos recibidos son: %*
echo El primer argumento es %1
echo El segundo argumento es %2
echo El tercer argumento es %3

REM Calcular el numero de Argumentos

set num_arg=0
for %%a in (%*) do (
	set /a num_arg+=1
)

echo El numero de argumentos es %num_arg%