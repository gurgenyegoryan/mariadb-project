#!/bin/bash

apt update
apt install software-properties-common
add-apt-repository ppa:deadsnakes/ppa -y
apt install python3.9 -y
<<<<<<< HEAD
apt install -y python3-pip
=======
apt install -y python3-pip
>>>>>>> 590b5efe680153aa9e9d84a8ba4186df198d6ef7
