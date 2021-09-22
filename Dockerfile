FROM python:3.7-alpine
# 1. running python in unbuffered mode which is recomended when running python within docker containers
ENV PYTHONUNBUFFERED 1 

# 2. from out requirements.txt file copy to docker image file
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 

# 3. making directory within our Docker image that we can use to store our application source code
# a.creating directory
RUN mkdir /meter_project
# b.go to this directory
WORKDIR /meter_project
# c.copy our app folder from local machine to app folder we just created on docker image
COPY ./meter_project /meter_project

# 4. Creating app user - for security purposes, otherwise our app using the root account
# create user, -D means user runs on our application only and not having home directory
RUN adduser -D user
# switch docker to this user
USER user