#!/bin/bash

#########################################
# Installing necessary packages and running the project
# Additionally executing test cases
# Python pyYaml will be installed using requirements file
#########################################

# You can install other packages using pip
# However, there is already a requirements file which take cares of it

printf "Installing requirements..... \n"
pip install -r requirements.txt
cd src || { echo "could not switch to src folder"; exit 1; }
python main.py
printf "Running test cases...... \n"
printf "Switching to test folder..... \n"
cd .. || { echo "could not switch to test folder"; exit 1; }
cd test || { echo "Please check your test folder path"; exit 1; }
python test.py
printf "Process finished! \n"

