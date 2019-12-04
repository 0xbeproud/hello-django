django 기본 설정.

### get host ip on mac
```bash

HOST_IP=`docker run busybox ping -c 1 docker.for.mac.localhost | awk 'FNR==2 {print $4}' | sed s'/.$//'`
echo ${HOST_IP}

```

### install mysqlclient
```bash
~/labs/81k/django-api develop*
(venv) venv ❯ export LIBRARY_PATH="$LIBRARY_PATH:/usr/local/opt/openssl/lib/"

~/labs/81k/django-api develop*
(venv) venv ❯ pip install mysqlclient
Requirement already satisfied: mysqlclient in ./venv/lib/python3.6/site-packages (1.4.1)

or

LDFLAGS="-L/usr/local/opt/openssl/lib" pip install mysqlclient
```

### run celery beat and worker

```bash
celery -A djangoapi beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery -A djangoapi worker -l info  --loglevel=DEBUG
```
