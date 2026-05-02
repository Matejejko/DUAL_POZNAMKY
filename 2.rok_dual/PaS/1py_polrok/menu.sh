#!/usr/bin/env bash

echo menu

clear

volba=0
while [ "$volba" -ne 5 ]
do
    echo " "
    echo "===== MENU ====="
    echo "1 - meno a aktualna cesta"
    echo "2 - vypis IPv4 adrie"
    echo "3 - vypis nazov linuxu"
    echo "4 - vykonaj prikaz"
    echo "5 - exit"
    echo "================"

    read -p "zadaj volbu: " volba
case "$volba" in
	1)
        whoami && pwd
        exit
    	shift
        ;;
	2)
	    ip a | grep -w "inet" | awk -F' ' '{print $2}'		
	    shift
		;;
	3)
		cat /etc/os-release | awk NR==1 | awk -F'=' '{print $2}' | tr -d \"
		shift
		exit
		;;
	4)
		prikaz=0
		read -p "zadaj command: " prikaz 
	 	$prikaz
		exit
		shift
		;;
esac

done

