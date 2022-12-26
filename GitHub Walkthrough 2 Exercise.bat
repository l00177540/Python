# By: LOC
# Date: 27/11/2022
# Function: Perform a commit
# Script: Walkthough 2 Exercise.bat
# This is the .bat file version of the Linux shell
# script provided on page 12 of Git Walkthrough 3
git status
echo "**************************************************"
echo Performing an add for all files in this directory"
echo "**************************************************"
git add .
git status
echo "**************************************************"
set /p MESSAGE=Please enter the commit message:
git commit -m "$MESSAGE"
git status
echo "**************************************************"
echo "Pushing to GITHUB repository"
git push -u origin main
echo "**************************************************"
echo "Done!"
cmd /k

