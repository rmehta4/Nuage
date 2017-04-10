# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Rutvij Mehta

#Install pip flask
RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install Flask-PyMongo

# Expose port
EXPOSE  5001

# Set the default command to execute when creating a new container
ENTRYPOINT ["python"]
CMD ["todo.py"]
