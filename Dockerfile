FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python-pip python-dev

WORKDIR /app/getemp
ADD . /app/getemp

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python", "GetEmp.py"]
