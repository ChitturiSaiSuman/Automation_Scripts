# Commit changes to Main Branch
#!/usr/bin/env bash
git config --global user.name "ChitturiSaiSuman"
git config --global user.email "saisumanchitturi@gmail.com"
git add .
git status
read -p 'Commit Message: ' message
echo "Your Github token: "
cat /home/suman/Git/Token.txt
git commit -m "$message"
git push
echo "Uploaded Successfully"
sleep 5
clear
