import os
from secret import DATASET_RESULT_ID, WORKFLOW_ID

def get_result():
    os.system('gradient datasets files get --id "' + DATASET_RESULT_ID + '" --target-path "pipeline_result/"')
        
def run_pipeline():
    os.system('gradient workflows run --id ' + WORKFLOW_ID + ' --path yolo_pipeline.yaml')

if __name__ == "__main__":
    #run_pipeline()
    get_result() #Danger les versions !!