# Docker file for ct_covidnet ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/pl-CT-covidnet .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-CT-covidnet .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-CT-covidnet
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-CT-covidnet
#



FROM fnndsc/ubuntu-python3:18.04
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/ct_covidnet"
ENV DEBIAN_FRONTEND=noninteractive
COPY ["ct_covidnet", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN apt-get update \
  && apt-get install -y libsm6 libxext6 libxrender-dev python3-tk\
  && pip install --upgrade pip \
  && pip install -r requirements.txt


CMD ["ct_covidnet.py", "--help"]