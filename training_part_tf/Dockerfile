FROM tensorflow/tensorflow:2.5.0-gpu

RUN apt-get update && yes | apt-get upgrade
RUN mkdir -p /tensorflow/models
RUN apt-get install -y git python3-pip
RUN pip install --upgrade pip
RUN pip install tensorflow==2.5.0

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y protobuf-compiler python-pil python-lxml

RUN pip install matplotlib
RUN git clone https://github.com/tensorflow/models.git /tensorflow/models

WORKDIR /tensorflow/models/research

RUN protoc object_detection/protos/*.proto --python_out=.

RUN export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim