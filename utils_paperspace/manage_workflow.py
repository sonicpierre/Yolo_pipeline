import sys
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import API_KEY
from gradient import DatasetVersionsClient, WorkflowsClient, ProjectsClient

datasetVersions_client = DatasetVersionsClient(API_KEY)
workflow_client = WorkflowsClient(API_KEY)
projects_client = ProjectsClient(API_KEY)

def create_or_recup_workflow(name:str, project_name:str):
    """
    Permet de récupérer le workflow 
    """

    project_id = None
    for project in projects_client.list():
        if project.name == project_name:
            project_id = project.id

    liste_wf = workflow_client.list(project_id=project_id)
    wf = liste_wf[0].id if len(liste_wf) > 0 else workflow_client.create(name=name, project_id=project_id)

    return wf