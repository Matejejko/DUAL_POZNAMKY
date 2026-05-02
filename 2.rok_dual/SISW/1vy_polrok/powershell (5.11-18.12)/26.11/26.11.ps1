#1. FORMATING -F operator

"{0:N2} GB" -f ((Get-ChildItem "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\2.rok_dual-main\" -Recurse -Force | Measure-Object -property length -sum).sum / 1Gb)
# N2 -> specifikuje typ formatovania

$velkost = (Get-ChildItem "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\2.rok_dual-main\" -Recurse -Force | Measure-Object -property length -sum)
$tmp = [system.math]::Round($velkost.Sum/1Gb,2)
Write-Host "celkova velkost cesty je $($tmp) GB"

#2. FORMATING 
    # niekedy je dobre mat vysledky v tabulke a niekedy v liste
    # ak to chceme zmenit na konci dame " | Format-... "

    # musi byt vzdi na konci lebo defakto uz je to text

get-service | Select-Object -First 3 | Select-Object * | Format-list

Get-Service | Where-Object {$_.StartType -eq "Automatic" -AND $_.Status -ne "Running"} | Ft -Property Name,Status



#input / output
#konzolovy vstup/vystup ->> read-host/write-host
#1.
Get-Service | Where-Object {$_.StartType -eq "Automatic" -AND $_.Status -ne "Running"} | 
Select-Object -Property name,displayname,status,starttype |
Out-File -FilePath "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.txt" -force -width 250

Test-Path -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.txt"

Get-Content -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.txt" | Format-list

#ak to uz ulozime do suboru tak uz to je ako string a dalsie spracovanie je prakticky nemozne 


#2. CSV vystup/vstup

Get-Service | Where-Object {$_.StartType -eq "Automatic" -AND $_.Status -ne "Running"} | 
Select-Object -Property name,displayname,status,starttype |
Export-Csv -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.csv" 

Test-Path -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.csv"

Import-Csv -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.csv" | Select-Object name,status

$tmp = Import-Csv -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.csv"

#oproti txt tak vsetko zahinulo ako txt ale zostali nam properties


#3. XML vystup/vstup
Get-Service | Where-Object {$_.StartType -eq "Automatic" -AND $_.Status -ne "Running"} | 
Select-Object -Property name,displayname,status,starttype |
Export-Clixml -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.xml"

Test-Path -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.xml"

$tmp = Import-Clixml -Path "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.xml"

#ak budeme robit export kde dalej niekto ho bude upravovat, tak najvhodnejsie je tento format


#HTML format
#je idealny na pekne formatovanie

Get-Service | Where-Object {$_.StartType -eq "Automatic" -AND $_.Status -ne "Running"} | 
Select-Object -Property name,displayname,status,starttype |
ConvertTo-Html -Title "stav automatic servisov" | Out-File "C:\Users\A200354239\OneDrive - Deutsche Telekom AG\Desktop\services.html"



