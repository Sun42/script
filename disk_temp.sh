#!/bin/sh

HDD_TEMP=`sudo hddtemp /dev/sda1 | cut -d ' ' -f 4`
echo "HDD: $HDD_TEMP"
