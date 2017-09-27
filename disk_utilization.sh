#!/bin/sh

DISK_UTILIZATION=`iostat -N -h -d sda -x | tail -n 2 | head -n 1 | awk '{print $13}'`
echo "HDD: $DISK_UTILIZATION%"
