#!/bin/sh

LOAD=`cat /proc/loadavg | cut -d ' ' -f 1,2,3`

echo "LOAD: $LOAD"
