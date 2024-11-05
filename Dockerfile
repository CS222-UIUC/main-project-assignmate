FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

RUN sudo apt update
RUN sudo apt install python3
RUN sudo apt install python3-pip -y
RUN curl -sL https://deb.nodesource.com/setup_23.x | sudo -E bash -
RUN sudo apt install nodejs

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

WORKDIR "/frontend"

RUN npm install
