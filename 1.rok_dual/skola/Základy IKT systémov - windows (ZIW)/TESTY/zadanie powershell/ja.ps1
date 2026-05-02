$baseFolder = "C:\Users\A200354239\Downloads\Docasny"

New-Item -ItemType Directory -Path C:\Users\A200354239\Downloads -Name Docasny

1900..2024 | ForEach-Object {
    $yearFolder = Join-Path -Path $baseFolder -ChildPath $_
    New-Item -ItemType Directory -Path $yearFolder    
}

$Data = Import-Csv -Path C:\Users\A200354239\Downloads\powershell-netflix-2019.csv -Delimiter ';'

foreach ($row in $Data) {
    $showName = $row.ShowName
    $releaseYear = $row.ReleaseYear

    $yearFolder = Join-Path -Path $baseFolder -ChildPath $releaseYear
    $showFolder = Join-Path -Path $yearFolder -ChildPath $showName

    New-Item -ItemType Directory -Path $showFolder -Force
}
    
