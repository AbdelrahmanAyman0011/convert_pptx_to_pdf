#!/bin/bash

set -e

echo "installing Powerpoint convertor"


echo "first check needed libraries::"
#sudo apt update
sudo apt install -y libreoffice python3


echo "add it to local env:: "

sudo cp powerconvert.py /usr/local/bin/powerconvert

sudo chmod +x /usr/local/bin/powerconvert


echo "installation complete ;)"

