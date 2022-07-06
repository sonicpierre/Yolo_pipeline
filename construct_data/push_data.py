from gradient import DatasetsClient, DatasetVersionsClient, StorageProvidersClient
import sys
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import API_KEY, create_file_insert
import os
import json

datasets_client = DatasetsClient(API_KEY)
datasetVersions_client = DatasetVersionsClient(API_KEY)
storage_provider_client = StorageProvidersClient(API_KEY)

def define_dataset(name:str):

    sid=None
    for storage_provider in storage_provider_client.list():
        if storage_provider.name == "Gradient Managed":
            sid=storage_provider.id

    id_dataset = datasets_client.create(
        name=name,
        storage_provider_id=sid
    )

    create_file_insert(("Id dataset", id_dataset))
    

def define_version_upload(data_path:str, name_json="data_secret.json"):
    
    with open(name_json) as json_file:
        dico_info = json.load(json_file)

    version = datasetVersions_client.create(
        dataset_id=dico_info["Id dataset"]
    )
    
    os.system("gradient datasets files put --id '" + dico_info["Id dataset"] + ":" + version + "' --source-path " + data_path)
    os.system("gradient datasets versions commit --id '" + dico_info["Id dataset"] + ":" + version + "'")
    create_file_insert(("Version",version))

def visualise(name_json="data_secret.json"):

    with open(name_json) as json_file:
        dico_info = json.load(json_file)

    os.system("gradient datasets files list --id '" + dico_info["Id dataset"] + ":" + dico_info["Version"] + "'")
    

if __name__=='__main__':

    define_dataset("my_thumb")
    #define_version_upload("thumb/")
    #visualise()