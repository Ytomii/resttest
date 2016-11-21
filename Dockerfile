
# Set the base image to DEBIAN
FROM debian
MAINTAINER ME

# Update the sources list
RUN apt-get update && \
	apt-get install -y  git \
				python \
				python-pip && \
	pip install flask flask-httpauth



# Git clone app
ARG CACHEBUST=1
RUN git clone https://github.com/Ytomii/resttest.git

# Get pip to download and install requirements:

# Expose ports
EXPOSE 5000

# Set the default directory where CMD will execute
WORKDIR /resttest

# Set the default command to execute    
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python app.py