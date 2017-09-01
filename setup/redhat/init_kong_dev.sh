#!/bin/bash

role=`id -u`
if test $role -ne 0
then
    echo "Root permissions are required"
    exit 1
fi

cd ~

yum install -y luarocks lua-devel openssl-devel
luarocks install busted
luarocks install lua-llthreads2


yum install "https://bintray.com/kong/kong-community-edition-rpm/download_file?file_path=dists/kong-community-edition-0.11.0.el7.noarch.rpm"

echo "PATH=$PATH:/usr/local/openresty/bin/:/usr/local/openresty/nginx/sbin" >> ~/.bash_profile
echo "export PATH" >> >> ~/.bash_profile
echo "ulimit -n 8192" >>  ~/.bash_profile
source ~/.bash_profile

yum install -y git
git clone https://github.com/Mashape/kong.git


yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
yum install -y postgresql96
yum install -y postgresql96-server

/usr/pgsql-9.6/bin/postgresql96-setup initdb
systemctl enable postgresql-9.6
systemctl start postgresql-9.6

cd /tmp
sudo -u postgres createuser kong
sudo -u postgres createdb -O kong kong
sudo -u postgres createdb -O kong kong_tests


cd kong
luarocks make
make dev
make test

