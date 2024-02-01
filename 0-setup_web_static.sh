#!/usr/bin/env bash
# sets up your web servers for deployment of the web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo -e "<html>
<head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
f=/etc/nginx/sites-available/default
line="location /hbnb_static/{\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "27i $line" $f
sudo service nginx restart
