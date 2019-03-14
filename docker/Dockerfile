#DOCKERFILE for installing Ubuntu Xenial with the starwars api

FROM ubuntu:xenial
MAINTAINER Waleed Hammam

# updating repos
RUN echo 'updating repos'
RUN apt-get update

#installing pip3
RUN echo 'installing pip3'
RUN apt-get -y install python3-pip

#installing git 
RUN echo 'installing GIT'
RUN apt-get -y install git

#clonning the dashboard repo
RUN echo 'clonning the repo'
RUN git clone https://github.com/waleedhammam/star_wars.git

#installing requirements
RUN echo 'installing python requirment'
RUN cd star_wars && pip3 install -r requirments.txt

# exposing port 5001 and running the server
EXPOSE 5001
CMD cd /star_wars/ && python3 server.py
