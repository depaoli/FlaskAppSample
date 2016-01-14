# Includes the Flask Application Server
FROM depaoli/flaskappserver

MAINTAINER Matteo De Paoli <depaoli@>

#
# Install the Python Package inside the FlaskAppServer and indicate the configured port
#
RUN pip install git+https://github.com/depaoli/FlaskAppSample.git
EXPOSE 2105
