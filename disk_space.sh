#!/bin/sh

DISK_USAGE=`df -h /home | tail -n 1 | awk '{print $3"/"$2, $5}'`
echo "HDD: $DISK_USAGE"
