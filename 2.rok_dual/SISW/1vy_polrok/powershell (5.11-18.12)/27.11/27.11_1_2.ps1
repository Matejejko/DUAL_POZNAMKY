<# 
about SIMPLE functions

function Calc (parameters) {
    script block
}
#>

function calc ($x,$y) {
    write-host "vykona sa sucet zadanych cisel $x a $y"
    $out = $x + $y
    $out
    
}

#aktivujeme ju tak ze vlozime do terminalu a enter nic nespravi ale vieme ju ptm volat s "calc"


<# 
about ADVANCED functions
#>


function Start-StoppedService {
<#
.Synopsis
   funkcia zobrazuje stav definovaneho servisu/sov a umoznuje ich restartovat.
.PARAMETER <ServiceName>
.DESCRIPTION
   funkcia ocakava MENO jedneho alebo viacerych windows servisov.
   vzdy vykona analyzu servisov a vypis do konzoly.
   ak uzivatel chce restartnut servis/y umozni mu to cez prompt.
   Uzivatel moze zadat RESTART  cez y/Y.
.INPUT
   Funkcia ocakava EXISTUJUCI servis alebo servisy (ich mena)
.OUTPUT
   Funkcia robi vypis do konzoly (konzola APP)
.EXAMPLE
   Start-StoppedService -name wuauserv
    
    Status   Name               DisplayName                           
    ------   ----               -----------                           
    Stopped  wuauserv           Windows Update                        
    chces tento servis RESTARTNUT? (Y/N): y
.NOTES
    SupportedOS: Windows ...
    Lastupdate: xxxx
    LastUpdateDate: xx.yy.oooo
    History: xx...
#>

    [CmdletBinding()] #umozni aby sa funkcia tvarila ako commandlet
    
    Param(
        # Parameter pre zadanie mena servisu
        [Parameter(Mandatory=$true,
                   Position=0)]
        [string[]]$ServiceName
    )

    Begin{
        clear-host
        Write-Host "####################" -ForegroundColor Cyan
        Write-Host " My first function" -ForegroundColor Cyan
        Write-Host "        v1.0" -ForegroundColor Cyan
        Write-host "     Autor MATEJ" -ForegroundColor Cyan
        Write-host "####################" -ForegroundColor Cyan
    }
     Process{
        #1) Zisit stav servicu
            Write-Host " "
            Write-Host "Zvolený service má takýto status:" -ForegroundColor Magenta
            Get-Service -Name $ServiceName

        if($ServiceName.Count -eq 1){
            #2) Restart/Start servicu
                Write-Host " "
                $UserInput = Read-Host "`nChceš tento service REŠTARTNÚŤ (y/n) ?"
                if ($UserInput -eq "y" -or "$UserInput" -eq "Y"){
                    Write-Host "`nVyžiadal si REŠTART servicu" -ForegroundColor Red
                    Restart-Service -Name $ServiceName -WhatIf
                }else{
                    Write-Host "`nNevyžiadal si reštart servicu" -ForegroundColor Green
                }

        }else{
            #3) Restart/Start viacerych servicov
                $UserInput = Read-Host "`nChceš tieto servicy REŠTARTNÚŤ (y/n) ?"
                if ($UserInput -eq "y" -or "$UserInput" -eq "Y"){
                    Write-Host "`nVyžiadal si REŠTART servicov" -ForegroundColor Red
                    Restart-Service -Name $ServiceName -WhatIf
                }else{
                    Write-Host "`nNevyžiadal si reštart servicov" -ForegroundColor Green
                }
        }
    }

    End{
        Write-Host "`nFunkcia bola ukončená" -ForegroundColor Yellow
    }
}
