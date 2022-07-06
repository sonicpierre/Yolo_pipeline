import os
import json
import shutil
import sys
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import API_KEY, PROJECT_NAME, create_file_insert
from gradient import DatasetVersionsClient, WorkflowsClient, ProjectsClient

datasetVersions_client = DatasetVersionsClient(API_KEY)
workflow_client = WorkflowsClient(API_KEY)
projects_client = ProjectsClient(API_KEY)

def create_or_recup_workflow(name:str, project_name:str):

    project_id = None
    for project in projects_client.list():
        if project.name == project_name:
            project_id = project.id

    liste_wf = workflow_client.list(project_id=project_id)
    if len(liste_wf) > 0:
        wf = liste_wf[0].id
    else:
        wf = workflow_client.create(name=name, project_id=project_id)

    create_file_insert(("Id Workflow", wf))

def clean_result():
    """
    Supprime l'ancien jeux de résultats
    """

    if os.path.exists("pipeline_result"):
        shutil.rmtree("pipeline_result")

    os.mkdir("pipeline_result")

def run_pipeline(name_json="data_secret.json"):
    """
    Lance la pipeline entière
    """
    with open(name_json) as json_file:
        dico_info = json.load(json_file)

    os.system('gradient workflows run --id ' + dico_info['Id Workflow'] + ' --path yolo_pipeline.yaml')


if __name__ == "__main__":
    create_or_recup_workflow("YoloWorkflow", PROJECT_NAME)
    clean_result()
    run_pipeline()