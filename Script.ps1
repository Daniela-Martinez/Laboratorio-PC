function option 
{
$opc = Read-Host -Prompt '¿Que desea ver? [1] Informe meteorologico [2] Clima de alguna ubicacion [3] Fase de la luna'
if($opc -eq 1){
option-1 } 
elseif ($opc -eq 2) {
option-2 } 
elseif  ($opc -eq 3) { 
option-3 }
else { 
break }
}
function option-1
{
$met = (curl http://wttr.in/?Q0"&"lang=es -UserAgent "curl" ).Content
Write-Host "$met"
}
function option-2
{
$ub = Read-Host 'Ingrese el nombre: '
$tie = (curl http://wttr.in/-$ub-?lang=es -UserAgent "curl" ).Content
Write-Host "$tie"
}
function option-3
{
$luna = (curl wttr.in/Moon@2017-07-13?lang=es -UserAgent "curl" ).Content 
Write-Host "$luna"
}






























