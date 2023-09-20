FROM ubuntu:latest

EXPOSE 3005

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install -r requirements.txt

WORKDIR "/app/src"
ENTRYPOINT [ "python3", "ThermostatServer.py" ]
