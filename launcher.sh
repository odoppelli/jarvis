#!/bin/sh
# launcher.sh

if [ "$(id -un)" != "pi" ]; then
	exec sudo -u pi $0 "$@"
fi

export DISPLAY=:0
export XAUTHORITY=/home/pi/.Xauthority

cd /home/pi/jarvis
sudo python3 -i gui1_4.py
