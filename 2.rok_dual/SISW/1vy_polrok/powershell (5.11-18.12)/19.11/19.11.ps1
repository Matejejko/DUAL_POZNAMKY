<#
Set-Alias -Name gs -Value Get-Service

$services = Get-Service
$services

$AutomaticServices = Get-Service | Where-Object {$_.StartType -ne "Automatic"}

[int]$Vek = Read-Host "Zadaj svoj vek"

New-Variable -Name Vek2 -Value 20 -Option ReadOnly

#zmena hodnoty
$Vek = 100

$Vek * $Vek2

$a = "I love PowerShell"
$a.Replace('PowerShell','Bash')

$a.ToUpper()
$a.ToLower()

$AllInfo = systeminfo
$OSVersion = (($AllInfo[3] -split ":")[-1]).Trim()
$OSVersion

$HashTable = @{name='Jano';value='18'}
#>


<#
loops - foreach-object
... | ForEach-Object -Begin {scriptA} -Process {scriptMain} -End {ScriptB}
#>

Get-Service | ForEach-Object {
    Write-Host "Meno servisu je $($_.DisplayName)"
}

<#
loops - foreach
ForEach($item in $Array){ScriptBlock}
#>

$services = Get-Service
foreach($item in $service){
    Write-Host "Meno servisu je $($_.DisplayName)"
}

<#
loops - For
For($init; Condition; Interakcia){script}
#>

$services = Get-Service
for($i=0; $i -lt $services.Count; $i++){
    Write-Host "Meno servisu je $($Services[$i].DisplayName)"
}



$x = 0
do{
    Write-Host "Meno servisu je $($services[$x].DisplayName)"
    $x++
}
until ($x -eq $services.Count)

$x = 0
do{
    Write-Host "[$x]Meno servisu je $($services[$x].DisplayName)"
    $x++
}
until ($x -lt $services.Count)