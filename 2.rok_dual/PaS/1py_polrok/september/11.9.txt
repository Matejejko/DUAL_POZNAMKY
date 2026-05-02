#!/usr/bin/env bash
whoami
pwd
date
echo "testovaci text"
echo "--------------------------"
echo "nazov skriptu: $0"
echo "prvy argument: $1"
read -p "Meno: " name
age=32
echo "Meno: $name Vek: $age"

datum="$(date)"

echo "$datum"

moja_cesta="$(realpath $0)"

echo "$moja_cesta"

moj_adresar="$(dirname "$moja_cesta" )"

echo "$moj_adresar"

moj_adresar_test="$( dirname  $( realpath $0 ) )"

echo "$moj_adresar_test"
