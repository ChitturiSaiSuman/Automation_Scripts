protonvpn-cli login saisumanchitturi
protonvpn-cli connect

echo "Do you wanna Disconnect? (Y/N)..."

read user_input

if [ "$user_input" == "y" ]
then
	protonvpn-cli disconnect
else
	echo "VPN is still connected"
	echo "Disconnect using protonvpn-cli disconnect command"
fi


