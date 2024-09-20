@echo off

REM *********************************

set value=%1%
set result=0
echo Calculando la media entre 1 y %value%

setlocal enabledelayedexpansion
for /L %%i in (1 1 %value%) do (
	set /a result+=%%i
	echo En la iteracion %%i la media vale %result% o !result!
)

set /a result/=value 
echo La media es %result%
endlocal
REM endlocal