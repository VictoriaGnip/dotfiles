#!/usr/bin/env python3

import json
import os
import sys
import time

from pprint import pprint

from wrappers import digitalocean


# TODO 1: Write a module for AWS Lightsail.
# TODO 2: Write an error handler.

def spin_up():
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc) # FIXME
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = 'do' # FIXME Parameter hard-coded to expedite testing.
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass # TODO 1
        elif vendor_choice in digital_ocean:
            # print(digitalocean.builder())
            os.system('{unix_command} > {writeout_file}'             \
                        .format(unix_command=digitalocean.builder(), \
                                writeout_file=writeout_file))
            return writeout_file
    else:
        pass # TODO 2

def harden():
    response = json.load(open(spin_up()))
    return response
    # payloads = []
    # if 'droplets' in response: # TODO write logic to control for a single droplet
    #     payloads = response['droplets']
    # else:
    #     payloads = response['droplet']
    # ip_addresses = []
    # for payload in payloads:
    #     ip_addresses.append(digitalocean.get_host(payload['id']))
    # for ip_address in ip_addresses:
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'.format(ip_address=ip_address))
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'.format(ip_address=ip_address))
    #     os.system('scp /home/kenso/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/kensotrabing/authorized_keys'.format(ip_address=ip_address))
    #     os.system('sh -c \'echo "kensotrabing:$w0rdf!$H" > /home/kenso/dotfiles/setup/.credentials\'')
    #     os.system('scp /home/kenso/dotfiles/setup/.credentials root@{ip_address}:/home/kensotrabing/'.format(ip_address=ip_address))
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote2.sh'.format(ip_address=ip_address))
    # return ip_addresses

if __name__ == '__main__':
    print(harden())