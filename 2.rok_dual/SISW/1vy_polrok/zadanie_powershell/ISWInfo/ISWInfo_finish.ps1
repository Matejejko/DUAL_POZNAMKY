<#
Vytvor PowerShell script alebo funkciu, ktorá zobrazí výstupné údaje tak (informačná kvalita, jednotky i formát), ako je to uvedené v časti
VÝSTUP tohto zadania.
Script bude akceptovať vstupný param [string[]]ComputerName
#>

function Get-ISWInfo {

<#
.Synopsis
    Získanie informácií o nainštalovanom softvéri s hodnotou InstallState = 5
.DESCRIPTION
    Funkcia Get-ISWInfo slúži na zber informácií o nainštalovanom softvéri zo zadaných počítačov.
    Dáta sa zbierajú iba z online systémov (overenie pomocou Test-Connection).

    Výstupom je PSCustomObject obsahujúci:
      - názov počítača
      - názov aplikácie
      - verziu aplikácie
      - výrobcu
      - dátum inštalácie

    Voliteľne je možné uložiť výstup do CSV súboru pomocou prepínača -OutFile.
.EXAMPLE
    Get-ISWInfo
    Zobrazí nainštalovaný softvér na lokálnom počítači.
.EXAMPLE
    Get-ISWInfo -ComputerName PC01,PC02 -OutFile
    Zobrazí nainštalovaný softvér na zadaných počítačocha uloží výstup do súboru C:\Temp\ISWInfo\ISWInfo.csv
#>

    [CmdletBinding()]

    Param(
        [Parameter(Mandatory = $false, 
                   ValueFromPipelineByPropertyName = $true,
                   Position = 0)] 
        [string[]]$ComputerName = $env:COMPUTERNAME,

        [switch]$OutFile,

        [switch]$Help
    )

    Begin {
        #PRVÝ KROK: Ak používateľ zadal -Help, okamžite otvoríme dokumentáciu a ukončíme funkciu.
        #   - Zistíme, kde sa nachádza skript (pomocou $PSScriptRoot; ak sme v konzole, použijeme aktuálny priečinok).
        #   - Skontrolujeme, či existuje súbor ISWInfoHELP.html v tom istom priečinku.
        #   - Ak áno → otvoríme ho v predvolenom prehliadači pomocou Start-Process.
        #   - Ak nie → vypíšeme chybovú hlášku a ukončíme.
        if ($Help) {
            $scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { $PWD.Path }
            $helpFile = Join-Path -Path $scriptDir -ChildPath "ISWInfoHELP.html"

            if (Test-Path -Path $helpFile -PathType Leaf) {
                Write-Host "Otváram lokálnu dokumentáciu: $helpFile" -ForegroundColor Green
                try {
                    Start-Process -FilePath $helpFile | Out-Null
                } catch {
                    Write-Error "Nepodarilo sa otvoriť '$helpFile'. Chyba: $_"
                }
            } else {
                Write-Error "Dokumentácia nebola nájdená: $helpFile"
                Write-Host "Skontrolujte, či je súbor 'ISWInfoHELP.html' v rovnakom priečinku ako tento skript." -ForegroundColor Yellow
            }

            # ✅ NASTAVÍME FLAG → ostatné bloky sa preskočia
            $script:HelpRequested = $true
            return
        }

        #DRUHÝ KROK: Normálne spustenie – pripravíme prostredie.
        #   - Vyčistíme konzolu (Clear-Host).
        #   - Vypíšeme úvodný banner s názvom, verziou a autormi.
        #   - Inicializujeme prázdne polia:
        #       * $ALLData – na ukladanie údajov o softvéri z každého počítača,
        #       * $NotReachable – na zber názvov nedostupných počítačov.
        $script:HelpRequested = $false
        Clear-Host
        Write-Host "#########################" -ForegroundColor White
        Write-Host "    Installed Software   " -ForegroundColor Cyan
        Write-Host "           v1.0          " -ForegroundColor Cyan
        Write-Host " Autors: Dvarga, Mpapaj   " -ForegroundColor Cyan
        Write-Host "#########################" -ForegroundColor White

        $script:ALLData = @()          # Sem budeme pridávať riadky s údajmi o softvéri
        $script:NotReachable = @()     # Sem uložíme názvy počítačov, ktoré neodpovedajú na ping
    }

    Process {
        # ✅ AK BOL ZADANÝ -Help, PRESKOČ VŠETKO
        if ($script:HelpRequested) {
            return
        }

        #HLAVNÁ SLUČKA: Prejdeme každý zadaný počítač (aj ak je len jeden).
        foreach ($Computer in $ComputerName) {
            #KROK 3.1: Overíme, či je počítač online pomocou jedného ping-u (Test-Connection -Quiet).
            #   - Ak odpovie → pokračujeme na zber dát.
            #   - Ak neodpovie → pridáme ho do zoznamu $NotReachable a preskočíme ďalšie kroky pre tento počítač.
            if (Test-Connection -ComputerName $Computer -Count 1 -Quiet -ErrorAction SilentlyContinue) {
                Write-Host "Zber dát z počítača: $Computer" -ForegroundColor Magenta

                try {
                    #KROK 3.2: Načítame zoznam softvéru cez WMI triedu Win32_Product,
                    #            ale iba tie záznamy, kde InstallState = 5 („nainštalované“).
                    #   - Používame Select-Object na vybratie len potrebných vlastností: Name, Version, Vendor, InstallDate.
                    $software = Get-WmiObject -ComputerName $Computer -Class Win32_Product -ErrorAction Stop |
                                Where-Object { $_.InstallState -eq 5 } |
                                Select-Object Name, Version, Vendor, InstallDate

                    #KROK 3.3: Pre každú nájdenú aplikáciu vytvoríme vlastný PSCustomObject.
                    #   - Transformujeme InstallDate (ak existuje) z formátu "yyyyMMdd" na čitateľný "dd.MM.yyyy".
                    #   - Ak dátum chýba alebo je neplatný → nahradíme ho textom "Neznámy dátum".
                    #   - Vytvoríme usporiadaný hash (ordered) s vlastnosťami: ComputerName, Name, Version, Vendor, InstallDate.
                    #   - Z toho vytvoríme PSObject a pridáme ho do poľa $ALLData.
                    foreach ($app in $software) {
                        $niceDate = if ($app.InstallDate) {
                            try {
                                [datetime]::ParseExact($app.InstallDate, "yyyyMMdd", $null).ToString("dd.MM.yyyy")
                            } catch {
                                "Neznámy dátum"
                            }
                        } else {
                            "Neznámy dátum"
                        }

                        $row = [ordered]@{
                            ComputerName = $Computer
                            Name         = $app.Name
                            Version      = $app.Version
                            Vendor       = $app.Vendor
                            InstallDate  = $niceDate
                        }

                        $script:ALLData += New-Object -TypeName PSObject -Property $row
                    }
                } catch {
                    # Ak pri zbere dát nastane chyba (napr. prístup zamietnutý, WMI nefunguje), vypíšeme varovanie, ale nepretrhneme celý beh – pokračujeme ďalším počítačom.
                    Write-Warning "Chyba pri zbere dát z $Computer`: $_"
                }
            } else {
                # Počítač neodpovedal → pridáme ho do zoznamu nedostupných systémov.
                $script:NotReachable += $Computer
            }
        }
    }

    End {
        # ✅ AK BOL ZADANÝ -Help, PRESKOČ VŠETKO
        if ($script:HelpRequested) {
            return
        }

        #KROK 4: Po spracovaní všetkých počítačov vypíšeme výsledky.

        #4.1: Ak sme niečo načítali → vypíšeme tabuľku do konzoly (PowerShell automaticky vyrenderuje objekty ako tabuľku).
        if ($script:ALLData.Count -gt 0) {
            $script:ALLData
        } else {
            Write-Host "Žiadne údaje neboli získané." -ForegroundColor Yellow
        }

        #4.2: Ak sa našli nedostupné počítače:
        #   - Uložíme ich zoznam do súboru C:\Temp\NotReachable.txt (prepíšeme existujúci).
        #   - Informujeme používateľa o počte a umiestnení súboru.
        if ($script:NotReachable.Count -ne 0) {
            $NotReachable | Out-File C:\TEMP\NotReachable.txt -Force
            notepad C:\TEMP\NotReachable.txt
            Write-Host "Niektoré počítače nie su dostupné. Zoznam uložený do: C:\TEMP\NotReachable.txt" -ForegroundColor Red
        }

        #4.3: Ak bol zadaný prepínač -OutFile A zároveň máme nejaké dáta:
        #   - Exportujeme $ALLData do CSV súboru C:\Temp\ISWInfo.csv (bez typovej hlavičky, prepíšeme existujúci).
        #   - Informujeme používateľa o úspešnom uložení.
        if ($OutFile -and $script:ALLData.Count -gt 0) {
            $csvPath = "C:\Temp\ISWInfo.csv"
            $script:ALLData | Export-Csv -Path $csvPath -NoTypeInformation -Force
            Write-Host "Výstup uložený do: $csvPath" -ForegroundColor Green
        }

        #4.4: Záverečná správa – ukončenie behu.
        Write-Host "Kód bol ukončený." -ForegroundColor Cyan
    }
}

 