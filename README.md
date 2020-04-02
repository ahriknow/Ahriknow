# System.

```shell script
docker container run --name ahriknow \
-e MYSQL_HOST=host \
-e MYSQL_PASS=pass \
-e REDIS_HOST=host \
-e REDIS_PASS=pass \
-d ahriknow/ahriknow:v20200402
```