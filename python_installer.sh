#!/bin/bash

apt update\
&& install software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa -y \
&& apt install python3.9 -y \
&& apt install -y python3-pip \
&& apt install -y python3-pip