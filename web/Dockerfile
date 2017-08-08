FROM python:3.6
 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
 
COPY requirements.txt /usr/src/app/
COPY necessary_packages.txt /usr/src/app/
RUN cat necessary_packages.txt requirements.txt > total_requirements.txt
RUN pip install --no-cache-dir -r total_requirements.txt
 
COPY . /usr/src/app
