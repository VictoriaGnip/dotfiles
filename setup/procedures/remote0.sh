#!/usr/bin/env bash

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 4" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'

adduser --disabled-password --gecos "" vicgnip

usermod -aG sudo vicgnip

cp .nanorc /home/vicgnip/

mkdir -p /etc/ssh/vicgnip