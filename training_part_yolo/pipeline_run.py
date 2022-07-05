import os
import shutil
from secret import DATASET_RESULT_ID, WORKFLOW_ID, API_KEY
from gradient import DatasetVersionsClient

datasetVersions_client = DatasetVersionsClient(API_KEY)

def clean_result():
    """
    Supprime l'ancien jeux de résultats
    """

    if os.path.exists("pipeline_result"):
        shutil.rmtree("pipeline_result")
    os.mkdir("pipeline_result")

def get_result():
    """
    Récupère les résultats du modèle entraîné
    """

    version = datasetVersions_client.list(dataset_id=DATASET_RESULT_ID)[0].version
    os.system('gradient datasets files get --id "' + DATASET_RESULT_ID + ':' + version + '" --target-path "pipeline_result/"')
        
def run_pipeline():
    """
    Lance la pipeline entière
    """

    os.system('gradient workflows run --id ' + WORKFLOW_ID + ' --path yolo_pipeline.yaml')


if __name__ == "__main__":
    clean_result()
    run_pipeline()
    #get_result() #Attendre le changement de version pour le faire