import sys
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import WORKFLOW_CLIENT, PROJECTS_CLIENT


def create_or_recup_workflow(name:str, project_name:str):
    """
    Permet de récupérer le workflow 
    """

    project_id = None
    for project in PROJECTS_CLIENT.list():
        if project.name == project_name:
            project_id = project.id

    liste_wf = WORKFLOW_CLIENT.list(project_id=project_id)
    wf = liste_wf[0].id if len(liste_wf) > 0 else WORKFLOW_CLIENT.create(name=name, project_id=project_id)

    return wf