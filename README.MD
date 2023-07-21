# # Clone inside a folder named flask:
Why it is needed. Because Docker-compose creates service names like: "parent.folder.name"_"service.name" 
So django service/host name will be named "flask_flask"
and will use "http://flask_flask:8001" in other container code


// Installation Process
If it does not work for permission use "sudo" !

// Docker version: 4.2.3
// Python 3.10.6

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

# Set up a new project with a single application (needed only for creation of project)

django-admin startproject admin . // Note the trailing '.' character django-admin startproject [project_name][directory]

# Create the Docker network:
Before running the containers, we need to create the external network (my_network) that will be shared by both the "admin" and "main" folders.\

docker network create my_network

to delete:

docker network rm my_shared_network

# Docker-compose Commands [use sudo if needed]

docker-compose up -d  // -d for running in the background 

docker-compose ps // list

docker-compose down //down all the containers

# Go inside the docker container

docker-compose exec django sh

// Inside the container we can use any commands
// To create a new app 'products' use cmd

python manage.py startapp products

python manage.py makemigrations

python manage.py migrate

# After this project is up and running

# Install Postman to check API (not needed in production server)

sudo snap install postman

# RabbitMQ configuration and installation (CloudAMPQ)

Log in to CloudAMPQ
Create a team and create a (free tier) instance in it
Go into the instance
Copy the AMPQ URI (like amqps://sxhupzyl:***@armadillo.rmq.cloudamqp.com/sxhupzyl) 

My URL:
amqps://sxhupzyl:6qwtiY5A6CJKv3PTVQY651zRzHAb5nib@armadillo.rmq.cloudamqp.com/sxhupzyl

Use ENV File in docker-compose/ docker/ and use model  (Pending)

# first run django docker compose then flask docker compose

# Check which containers are running under the same network 
docker ps --filter "network=my_shared_network"