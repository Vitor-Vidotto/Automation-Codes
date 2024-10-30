@echo off
setlocal

set minutes=2
set /a seconds=minutes*60
set cancel=0

echo Desligamento programado para em 2 minutos.
echo Aperte Ctrl + C para cancelar.

:countdown
if %cancel%==1 goto end
cls
echo Desligando em %seconds% segundos...
echo Aperte Ctrl + C para cancelar....
echo Ele vai pedir para finalizar, Digite S
timeout /t 1 >nul
set /a seconds-=1
if %seconds% leq 0 goto shutdown
goto countdown

:shutdown
shutdown /s /t 0
exit

:end
echo Desligamento cancelado.
exit
