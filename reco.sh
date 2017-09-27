#!/bin/sh
INTERFACE="wlp2s0"
INTERFACE_USB="wlx18a6f70ef124"


# timeout 5 ping www.google.co.uk -c 1; echo $?
while [ 1 ]
do
sleep 1
timeout 5 ping www.google.co.uk -c 1
#timeout 5 ping www.google.com -c 1
ret=$?
echo $ret
if [ $ret -gt 0 ]
then
    echo "reco..."
    nmcli d disconnect $INTERFACE
    nmcli d connect $INTERFACE
fi
done
