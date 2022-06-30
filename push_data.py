from gradient import DatasetsClient, DatasetVersionsClient
from secret import API_KEY, BUCKET_ID
import os
import json

datasets_client = DatasetsClient(API_KEY)
datasetVersions_client = DatasetVersionsClient(API_KEY)


def create_file_insert(to_insert:tuple, name="data_secret.json"):

    if name not in os.listdir():
        with open(name, 'a') as outfile:
            json.dump({to_insert[0]:to_insert[1]}, outfile)
    else:
        with open(name) as json_file:
            data = json.load(json_file)
        
        data[to_insert[0]] = to_insert[1]
        with open(name, 'w') as outfile:
            json.dump(data, outfile)

def define_dataset(name:str) -> dict:

    id_dataset = datasets_client.create(
        name=name,
        storage_provider_id=BUCKET_ID
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

    #define_dataset("my_face")
    define_version_upload("data/")
    visualise()