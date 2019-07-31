FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python3-pip python3

WORKDIR /app
COPY ./requirement.txt ./requirement.txt
RUN pip3 install -r requirement.txt
COPY . /app
EXPOSE 80
ENTRYPOINT ["python3", "demoapp.py"]
