import sys
import os
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import DATASETS_CLIENT, DATASETS_VERSION_CLIENT, STORAGE_PROVIDER_CLIENT

def dataset_exist(name:str) -> bool:
    for dataset in DATASETS_CLIENT.list():
        if dataset.name==name:
            return True
    return False

def define_dataset(name:str) -> str:

    sid=None
    for storage_provider in STORAGE_PROVIDER_CLIENT.list():
        if storage_provider.name == "Gradient Managed":
            sid=storage_provider.id

    id_dataset = DATASETS_CLIENT.create(
        name=name,
        storage_provider_id=sid
    )

    return id_dataset
    

def define_version_upload(data_path:str, id_dataset:str):


    version = DATASETS_VERSION_CLIENT.create(
        dataset_id=id_dataset
    )
    
    os.system("gradient datasets files put --id '" + id_dataset + ":" + version + "' --source-path " + data_path)
    os.system("gradient datasets versions commit --id '" + id_dataset + ":" + version + "'")
    
    return version

def visualise(id_dataset:str, id_version:str):

    os.system("gradient datasets files list --id '" + id_dataset + ":" + id_version + "'")