// Installation Process

# Python Installaion

https://serverspace.io/support/help/install-python-latest-version-on-ubuntu-20-04/

# Docker and Docker-Compose Installation

sudo apt install docker.io docker-compose -y
systemctl start docker
systemctl enable docker
docker --version

# Docker without sudo

sudo groupadd docker
sudo gpasswd -a $USER docker
sudo service docker restart
docker context use default

# Create a virtual environment to isolate our package dependencies locally (Optional)

python3 -m venv env
source env/bin/activate # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment

pip install django
pip install djangorestframework

# Set up a new project with a single application

django-admin startproject admin . # Note the trailing '.' character [project_name][directory]

# Docker-compose Commands [use sudo if needed]

docker-compose up
