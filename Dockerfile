FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

RUN sudo apt update
RUN sudo apt install python3
RUN sudo apt install python3-pip -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

WORKDIR "/backend"
RUN pip install selenium
RUN pip install django
RUN pip install pytest
RUN pip install pytest-cov
RUN pip install django-allauth
RUN pip install python-dotenv
RUN pip install social-auth-app-django
RUN pip install canvasapi
RUN pip install pycodestyle
RUN pip install autopep8
RUN pip install pylint
RUN pip install canvasapi
RUN pip install django-rest-framework
RUN pip install pytest-django
RUN pip install chromedriver-py
RUN pip install webdriver-manager
RUN pip install python-dotenv