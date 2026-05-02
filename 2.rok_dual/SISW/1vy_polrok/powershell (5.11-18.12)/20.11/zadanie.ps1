$data = Get-Service | Sort-Object -Property status
$data | ForEach-Object {
    if($_.Status -eq "Running"){
        Write-Host $_.DisplayName -ForegroundColor Green
    } else {
        Write-Host $_.DisplayName -ForegroundColor Red
    }
}