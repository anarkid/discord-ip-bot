#!/bin/bash

cd ~/botscript
source myenv/bin/activate

sleep 10  # Wait 10 seconds after boot

while true; do
    python3 ip_bot.py >> /home/piuser/botscript/log.txt 2>&1
    sleep 86400  # Sleep for 1 day
done
