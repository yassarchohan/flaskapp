FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python3.8 && apt-get install -y python3-pip

WORKDIR /app/getemp
ADD . /app/getemp

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.8", "GetEmp.py"]
