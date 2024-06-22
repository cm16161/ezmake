#!/bin/bash

sudo mkdir -p /opt/ezmake/
sudo cp -r templates /opt/ezmake/
sudo cp ezmake.py /opt/ezmake/ezmake
sudo chown $USER /opt/ezmake
sudo ln -s /opt/ezmake/ezmake /usr/local/bin/ezmake
