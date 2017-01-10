# image
图片服务

* 微信
  * https://raw.githubusercontent.com/WALL-E/static/master/images/wx-big.jpg
  * https://raw.githubusercontent.com/WALL-E/static/master/images/wx-middle.jpg
  * https://raw.githubusercontent.com/WALL-E/static/master/images/wx-small.jpg

# setup
安装服务

* JDK
  * CentOS-7.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_jdk|bash
    ```

* Python27
  * CentOS-6.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_python27|bash
    ```

* Pip27
  * CentOS-6.x, CentOS-7.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_pip27|bash
    ```

* Supervisor
  * CentOS-6.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_supervisor|bash
    ```



* Cassandra
  * CentOS-7.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_cassandra|bash
    ```

* Kong
  * CentOS-7.x
    
    ```
    yum install -y http://oerp142a4.bkt.clouddn.com/kong-0.9.5.el7.noarch.rpm
    ```

* influxDB
  * CentOS-7.x
    
    ```
    yum install -y http://oerp142a4.bkt.clouddn.com/influxdb-1.0.0.x86_64.rpm
    ```

* OpenResty
  * CentOS-7.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_openresty|bash
    ```

* Harbor
  * CentOS-7.x
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/redhat/install_harbor|bash
    ```

  * Ubuntu-14-04.5
    
    ```
    curl https://raw.githubusercontent.com/WALL-E/static/master/setup/ubuntu/install_harbor|bash
    ```

* docker-machine

  ```
  wget http://oerp142a4.bkt.clouddn.com/docker-machine-Linux-x86_64_0.8.2
  mv docker-machine-Linux-x86_64_0.8.2 /usr/local/bin/docker-machine
  chmod +x /usr/local/bin/docker-machine
  ```
  
* docker-compose
 
  ```
  wget http://oerp142a4.bkt.clouddn.com/docker-compose-Linux-x86_64_1.8.0
  mv docker-compose-Linux-x86_64_1.8.0 /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
  ```
  
* consul
 
   ```
   wget http://oerp142a4.bkt.clouddn.com/consul_0.7.0_linux_amd64.zip
   unzip consul_0.7.0_linux_amd64.zip
   sudo cp consul /usr/local/bin/
   ```
