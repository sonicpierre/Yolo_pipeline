import os
from config import LABELMAP, LABELS, CONFIG, MODEL
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format


def read_pipeline(config_file:str):

    #config = config_util.get_configs_from_pipeline_file(config_file)
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    with tf.io.gfile.GFile(config_file, "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)

    return pipeline_config

def write_pipeline(pipeline_config):

    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile("pipeline.config", "wb") as f:                                                                                                                                                                                                                     
        f.write(config_text)


def config_model(config_file:str, labelmap_path:str, labels:str, model_path:str):

    pipeline_config = read_pipeline(config_file)
    pipeline_config.model.ssd.num_classes = len(labels)
    pipeline_config.train_config.batch_size = 8
    pipeline_config.train_config.fine_tune_checkpoint = os.path.join("/inputs/mymodel", model_path, 'checkpoint', 'ckpt-0')
    pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
    pipeline_config.train_input_reader.label_map_path= labelmap_path
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join("/inputs/tfrecordsmythumb/", 'train.record')]
    pipeline_config.eval_input_reader[0].label_map_path = labelmap_path
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join("/inputs/tfrecordsmythumb/", 'test.record')]
    
    write_pipeline(pipeline_config)


if __name__=="__main__":
    config_model(CONFIG, LABELMAP, LABELS, MODEL)