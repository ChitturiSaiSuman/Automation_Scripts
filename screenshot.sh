# Takes Screenshot for every 30 Seconds.
# Change the value to any Integer to apply corresponding Frequency

while true; do scrot -d 30 '%H:%M:%S.png' -e 'mv $f ~/Pictures/Screenshots/'; done
