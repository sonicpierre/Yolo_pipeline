PROTOC_ZIP=protoc-3.15.8-linux-x86_64.zip
curl -OL https://github.com/google/protobuf/releases/download/v3.15.8/$PROTOC_ZIP
unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
unzip -o $PROTOC_ZIP -d /usr/local include/*
rm -f $PROTOC_ZIP
cd /inputs/repomodels/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python -m pip install .
python object_detection/builders/model_builder_tf2_test.py
pip install tensorflow --upgrade
cd