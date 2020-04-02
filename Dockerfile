FROM python:3.8
MAINTAINER "ahri"<ahriknow@ahriknow.cn>
ENV MYSQL_HOST 127.0.0.1
ENV MYSQL_PORT 3306
ENV MYSQL_NAME ahriknow
ENV MYSQL_USER root
ENV MYSQL_PASS password
ENV REDIS_HOST 127.0.0.1
ENV REDIS_PORT 6379
ENV REDIS_PASS password
ENV REDIS_NAME_1 0
ENV REDIS_NAME_2 1
ADD ./ /project/Ahriknow
COPY pip.conf /etc/pip.conf
WORKDIR /project/Ahriknow
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 9000
ENTRYPOINT ["gunicorn", "-w", "2", "-b", "0.0.0.0:9000", "Ahriknow.wsgi"]