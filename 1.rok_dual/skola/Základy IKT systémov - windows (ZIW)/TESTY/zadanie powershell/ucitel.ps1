$shows = Import-Csv .\powershell-netflix-2019.csv -Delimiter ";"
mkdir Docasny

for ($i = 1900; $i -le 2025; $i++){
mkdir "Docasny\$i" 
}

foreach ($show in $shows){
$rok = $show.ReleaseYear
$nazov = $show.ShowName
mkdir "Docasny\$rok\$nazov"
}

