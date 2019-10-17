FROM python:latest
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip
COPY . /datagenerationservice
WORKDIR /datagenerationservice
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD python3 app.py