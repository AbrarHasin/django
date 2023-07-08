// Installation Process
If it does not work for permission use "sudo" !

# Python Installaion

https://serverspace.io/support/help/install-python-latest-version-on-ubuntu-20-04/

sudo apt install python-is-python3 // to make python command run python3

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

sudo apt install python3-pip
pip install django
pip install djangorestframework

export PATH="/bin/myscripts:$PATH" (for warning to add path)

# Set up a new project with a single application

django-admin startproject admin . // Note the trailing '.' character django-admin startproject [project_name][directory]

# Docker-compose Commands [use sudo if needed]

docker-compose up -d  // -d for running in the background 

docker-compose ps // list

docker-compose down //down all the containers

# Go inside the docker container

docker-compose exec backend sh

// Inside the container we can use any commands
// To create a new app 'products' use cmd

python manage.py startapp products

python manage.py makemigrations

python manage.py migration

# workflow

add serializer.py (if needed)

add fields to models.py

makemigrations and migrate

add views.py with CRUD functionalities

add urls.py URL paths