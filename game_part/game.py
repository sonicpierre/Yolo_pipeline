import gym
import shutil
import os
import sys
from gradient import DatasetVersionsClient, DatasetsClient, StorageProvidersClient
from ale_py.roms import Breakout
from ale_py import ALEInterface
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import API_KEY, DATASET_RESULT_NAME

datasetVersions_client = DatasetVersionsClient(API_KEY)
datasets_client = DatasetsClient(API_KEY)
storage_provider_client = StorageProvidersClient(API_KEY)

def get_result():
    """
    Récupère les résultats du modèle entraîné
    """

    data_id = None
    for dataset in datasets_client.list():
        if dataset.name == DATASET_RESULT_NAME:
            data_id = DATASET_RESULT_NAME

    if not data_id:
        sid=None
        for storage_provider in storage_provider_client.list():
            if storage_provider.name == "Gradient Managed":
                sid=storage_provider.id

        data_id = datasets_client.create(
            name=DATASET_RESULT_NAME,
            storage_provider_id=sid
        )
    
    if not os.path.exists("pipeline_result"):
        os.makedirs("pipeline_result")
    else:
        shutil.rmtree("pipeline_result")
        os.makedirs("pipeline_result")

    version = datasetVersions_client.list(dataset_id=data_id)[0].version
    os.system('gradient datasets files get --id "' + data_id + ':' + version + '" --target-path "pipeline_result/"')
    

def create_env():
    ale = ALEInterface()
    ale.loadROM(Breakout)
    env = gym.make('ALE/Breakout-v5',
                    obs_type='rgb',                   # ram | rgb | grayscale
                    frameskip=4,                      # frame skip
                    mode=None,                        # game mode, see Machado et al. 2018
                    difficulty=None,                  # game difficulty, see Machado et al. 2018
                    repeat_action_probability=0.25,   # Sticky action probability
                    full_action_space=True,          # Use all actions
                    render_mode="human"                  # None | human | rgb_array
    )
    env.reset()
    return env

if __name__ == "__main__":
    #get_result()
    print("Début jeux")