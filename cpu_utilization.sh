#!/bin/sh

CPU_UTILIZATION=`ps -A -o pcpu | tail -n+2 | paste -sd+ | bc`
echo "CPU: $CPU_UTILIZATION %"
