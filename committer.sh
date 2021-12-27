# Commit changes to Main Branch
#!/usr/bin/env bash
git config --global user.name "ChitturiSaiSuman"
git config --global user.email "saisumanchitturi@gmail.com"

git add .
git status
read -p 'Commit Message: ' message

git commit -m "$message"

python3 /home/suman/Automation_Scripts/Copy.py /home/suman/Git/Token.txt

git push
echo "Uploaded Successfully"
sleep 5
clear