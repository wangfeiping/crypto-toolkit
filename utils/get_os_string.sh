#!/bin/bash

#
# curl https://raw.githubusercontent.com/WALL-E/static/master/setup/unknown/prometheus/install_prometheus | bash
#
#
# Operating System (pass-test): 
#
# 
# 1. Ubuntu 20.04.2 LTS
# 2. Red Hat Enterprise Linux 8.4 (Ootpa)
# 3. Amazon Linux 2
#


if hostnamectl | grep "Amazon" >/dev/null 2>&1; then
    echo "amazon"
    exit
fi

if hostnamectl | grep "Ubuntu" >/dev/null 2>&1; then
    echo "ubuntu"
    exit
fi

if hostnamectl | grep "Red Hat" >/dev/null 2>&1; then
    echo "redhat"
    exit
fi

echo "linux"
