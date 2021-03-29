#!/bin/bash
# install_raspberry_pi.sh
# Installs base dependencies

echo "Installing base dependencies"
sudo apt-get -y install python-pip \
    libjack-dev \
    libasound2-dev \
    libasound2 \
    build-essential \
    python3-dev \
    python3-rpi.gpio

python -m pip install virtualenv
