<#
IF/Else
syntax:
if(condition){scriptblockA}
elseif(condition){scriptblockB}
else {scriptblockC}
#>

<#
$service = Get-Service webclient
Write-Host "service webclien ma aktualne status $($service.Status)." -Foreg Magenta
If($service.Status -ne "Running") {
    Write-Host "service webclient nebezi, bude spusteny." -Foreg Magenta
    Start-Service -Name $service.Name
    Get-Service wuauserv | Start-Service
    $service | Start-Service
} else {
    Write-Host "service webclient bezi, nevyzaduje akciu." -foreg Magenta
}

Get-Process Notepad | Stop-Process

#>

<#
switch
syntax:
    switch(RiadiacaPremenna){
        "HodnotaA" {ScriptBlockA}    #ak chceme aby sa ukoncil pri prvej zhode dame ku koncu ; break ->> {scriptblock; break}
        "HodnotaB" {ScriptBlockB}
        "HodnotaC" {ScriptBlockC}
        default {ScriptBlockD}
    }
#>

$servername = Read-Host "zadaj meno servera"
switch -Wildcard ($servername){
    "*MUC*" {Write-Host "server lokacia je Mnichov"}
    "*FFM*" {Write-Host "server lokacia je Frankfurkt"}
    "*LON*" {Write-Host "server lokacia je Londin"}
    "*SQL*" {Write-Host "server APP je SQL SERVER"}
    "*DC*" {Write-Host "server APP je Domain Controller"}
    "*DNS*" {Write-Host "server APP je DNS server"}
    default {Write-Host "neznamy server" -ForegroundColor Red}
}
