apt-get update && yes | apt-get upgrade
apt-get install -y git python3-pip
apt-get install ffmpeg libsm6 libxext6 -y
DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y protobuf-compiler python-pil python-lxml
cd /inputs/repomodels/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python3 -m pip install .
cd