# Shows current clock speed of CPU in MHz
# To stop execution, press the key Combination CTRL + c
while true
do
lscpu | grep "MHz";
sleep 0.33;
clear;
done
