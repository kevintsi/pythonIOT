FROM ubuntu:latest
WORKDIR /usr/src/app
RUN apt-get update && apt install python3 -y && apt install python3-pip -y && apt install vim -y
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000 
CMD ["python3", "./app.py"]
