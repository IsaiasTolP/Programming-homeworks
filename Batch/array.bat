@echo off

REM *********************************

set countries[0]=Suiza
set countries[1]=Reino Unido
set countries[2]=Suecia
set countries[3]=España
set countries[4]=Francia
set countries[5]=Ciudad del Vaticano
set n=5

setlocal enabledelayedexpansion
for /L %%p in (0 1 %n%) do (
	echo El pais numero %%p es !countries[%%p]!
)
endlocal

set n=19
set values[0]=8
set values[1]=6
set values[2]=3
set values[3]=43
set values[4]=123
set values[5]=23
set values[6]=54
set values[7]=66
set values[8]=77
set values[9]=45
set values[10]=67
set values[11]=1
set values[12]=9
set values[13]=63
set values[14]=76
set values[15]=54
set values[16]=32
set values[17]=45
set values[18]=254
set values[19]=13
for /L %%v in (0 1 %n%) do (
	set /a result+=values[%%v]
)

set /a result/=n
echo la media es %result%