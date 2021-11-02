# OutLearn
Outlearn Python Project
# Set up Python3 in the ubuntu 
# Follow the below commands to setup python 
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
# Python Package can be installed from below command 
pip3 install package_name
# Run below command to solve the dependency problem
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
# Now install the django 
pip install django
# After setup the above steps run the below command to run the server 
Python3 manage.py runserver 
# If you get any error related to the package dependency  run the below command 
pip3 install package_name
# Once all dependency is installed your server is started below is your base url.
localhost:8080

