FROM ubuntu
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python python3-pip wget git unzip -y
Workdir /opt/source-code/model
Run wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
Workdir /opt/source-code/
COPY . /opt/source-code/
RUN pip install -r requirements.txt
Entrypoint ["python3","main.py"]
CMD ["model/lid.176.bin"]
