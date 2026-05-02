#kod v PS, aby zobrazil info o volume C o jeho 
#vekosti[GB], volnom mieste [GB] a volnom mieste [%]

Get-Volume -DriveLetter C | Select-Object -Property @{
n="Size[GB]";e={[system.Math]::Round($_.Size/1Gb,2)}},@{
n="Remaining[GB]";e={[system.Math]::Round($_.SizeRemaining/1Gb,2)}},@{
n="utilization[%]";e={[system.Math]::Round($_.SizeRemaining/$_.Size*100,2)}}
