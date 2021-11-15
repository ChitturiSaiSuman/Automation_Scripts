# Commit changes to Main Branch
#!/usr/bin/env bash
# Testing this script
git config --global user.name "ChitturiSaiSuman"
git config --global user.email "saisumanchitturi@gmail.com"
git add .
git status
read -p 'Commit Message: ' message
git commit -m "$message"
git push
echo "Uploaded Successfully"
sleep 5
clear
