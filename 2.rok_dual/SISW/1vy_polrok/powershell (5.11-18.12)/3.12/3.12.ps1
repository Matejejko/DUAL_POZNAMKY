<#
vytvorte APP, ktora zobrazi info o systeme a to:
    - bios version
    - system serial no.
    - OS version
    - OS name    
#>

# CIM --> Powershell remoting, All products
# WMI --> proprietary (reakcia na CIM), iba Microsoft produkty, vzdy zacinaju s prefixom Win32


function Get-InfoData{

<#
.Synopsis
   Short description
.DESCRIPTION
   Long description
.EXAMPLE
   Example of how to use this cmdlet
.EXAMPLE
   Another example of how to use this cmdlet
#>

    [CmdletBinding()]

    Param(
        # Param1 help description
        [Parameter(Mandatory=$false, 
                   ValueFromPipelineByPropertyName=$true,
                   Position=0)] 
        [string[]]$ComputerName = $env:COMPUTERNAME,

        [switch]$OutFile

 
    )

    Begin{
        Clear-Host
        Write-Host "#####################" -ForegroundColor White
        Write-Host "  Computer INFO DATA"   -ForegroundColor Cyan
        Write-Host "        v1.0"          -ForegroundColor Cyan
        Write-Host "    Autor DVarga"      -ForegroundColor Cyan
        Write-Host "#####################" -ForegroundColor White

        $ALLData = @()
        $NotReachable = @()
    }

    Process{
        foreach($Computer in $ComputerName){
            if(Test-Connection -ComputerName $computer -Count 1 -Quiet -ErrorAction SilentlyContinue){
                #Zbieranie informácii o BIOSe a OS
                $bios = Get-WmiObject -ComputerName $Computer -Class win32_Bios | select SerialNumber,Version
                $OSData = Get-WmiObject -ComputerName $Computer -Class win32_OperatingSystem | select Version,Caption
                $HWData = Get-WmiObject -ComputerName $Computer -Class win32_ComputerSystem | select Manufacturer,Model

                Write-Host "Colllecting data from computer $computer" -ForegroundColor Magenta
                #Vytvorenie PSCustom objektu pre výstup
                $OneSystemInfo =[ordered] @{
                    ComputerName     = $Computer
                    BIOSVersion = $bios.Version
                    BIOSSerialNo    = $bios.SerialNumber
                    OSVersion    = $OSData.Version
                    OSName    = $OSData.Caption
                    HWModel = $HWData.Model
                    HWVendor = $HWData.Manufacturer
                    namevendor = $Computer + " " + $HWData.Manufacturer
                }
                $myObject = New-Object -TypeName psobject -Property $OneSystemInfo
                $ALLData += $myObject
            } else{
                $NotReachable += $Computer
            }
        }
    }

    End{
        #Výpis výsledku do konzoly
        Write-Host "Vystupne dáta zo systému $computer sú:" -ForegroundColor Magenta
        $ALLData

        Write-Host "Kód bol ukončený" -ForegroundColor Cyan
        #vypis nedostupnych systemov do suboru
        if($NotReachable.count -ne 0){
            $NotReachable | Out-File C:\TEMP\NotReachable.txt -Force
            notepad C:\TEMP\NotReachable.txt

            Write-Host "`nTieto systémy sú NEDOSTUPNÉ, pozri súbor C:\TEMP\NotReachable.txt" -ForegroundColor Red
        }

        if($OutFile){
            wirte-host "output bude vypisany do suboru C:\Temp\OutFile.csv"
            $ALLData | Export-Csv -Path 'C:\Temp\OutFile.csv' -NoClobber -NoTypeInformation -Force
        }
    }
}