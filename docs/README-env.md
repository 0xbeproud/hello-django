
### pip install mysqlclient
```bash
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
pip install mysqlclient
```

### create database
```mysql
CREATE DATABASE weproud CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
create user weproud@'%' identified by 'weproud123';
grant all privileges on weproud.* to weproud@'%' identified by 'weproud123';
```

### get docker host ip on mac
```bash

HOST_IP=`docker run busybox ping -c 1 docker.for.mac.localhost | awk 'FNR==2 {print $4}' | sed s'/.$//'`
echo ${HOST_IP}

```

### docker-compose up

```bash
~/labs/81k/django-api develop*
❯ docker-compose up --build
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

ERROR: Network weproud-net declared as external, but could not be found. Please create the network manually using `docker network create weproud-net` and try again.

~/labs/81k/django-api develop*
❯ docker network create weproud-net
50e610988b1b2a42abbca0aef8c9acd722fcd0ab81b4ebc3250836312b150c4f

~/labs/81k/django-api develop*
❯ docker-compose up --build
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating volume "django-api_weproud_data" with default driver
Building django
Step 1/9 : FROM python:3.6.4
```