# Shows current clock speed of CPU in MHz
# To stop execution, press the key Combination CTRL + C
while true
do
lscpu | grep "CPU MHz";
sleep 0.33;
clear;
done
