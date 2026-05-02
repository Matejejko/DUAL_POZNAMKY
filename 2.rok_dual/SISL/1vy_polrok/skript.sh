#! /bin/bash

#set -x

name=$(whoami)
datum=$(date)
pocet_procesov=$(ps -e --no-headers | wc -l)
cpu_load_1=$( uptime | awk -F',' ' {print $4}' | awk -F':' 'NR==1 {print $2}')
#cpu_load_2=$(sar -u 1 120 | awk '/Average/ {print 100 - $8}')
cpu_load_5=$(uptime | awk -F',' ' {print $5}')
mem_usage=$( free -m | awk 'NR==2 {print $3}')
sdb_read=$(iostat -dx | awk 'NR==4 {print $4}')
sdb_write=$(iostat -dx | awk 'NR==4 {print $3}')



echo "date: $datum"
echo "hostname: $name"
echo="=================="
echo "pocet procesov: $pocet_procesov"
echo "cpu load 1m: $cpu_load_1"
echo "cpu load 2m:"
echo "cpu load 5m: $cpu_load_5"
echo "mem used: $mem_usage Mb"
echo "sdb read: $sdb_read kb/s"
echo "sdb write: $sdb_write kb/s"