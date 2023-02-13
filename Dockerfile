FROM ubuntu
LABEL maintainer="Lee.J.H"
RUN apt-get update\
    && apt-get upgrade -y\
    && apt-get install wget python3 python3-pip -y \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\
    && apt -y install ./google-chrome-stable_current_amd64.deb\
    && pip install selenium \
    && pip install webdriver-manager


COPY ./test.py

