FROM ubuntu
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python python3-pip wget git unzip -y
Workdir /opt/source-code/
Run wget https://nlp.stanford.edu/data/glove.6B.zip
Run unzip glove.6B.zip
COPY . /opt/source-code/
RUN pip install -r requirements.txt
Entrypoint ["python3","flask_server.py"]
CMD ["glove.6B.100d.txt"]




