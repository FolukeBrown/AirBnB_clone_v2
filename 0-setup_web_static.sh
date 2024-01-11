#!/usr/bin/env bash
# A script that sets up web servers for deployment of web_static


# Installs nginx if not exist
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx restart

# Creates directories they do not already exist
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Creating html file
sudo touch /data/web_static/releases/test/index.html

# Adding content to html

echo "<html>
	<head>
	</head>
	<body>
	Holberton School
	</body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

# Creating symbolic link. Delete existing link and creates a new one everytime the script run
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Permissions
sudo chown -R ubuntu:ubuntu /data

# Nginx configuration
loc="server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "s/server_name _;/${loc}/" /etc/nginx/sites-available/default

# Restarting nginx
sudo service nginx restart
