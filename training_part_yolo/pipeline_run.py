import os
import sys
import argparse

sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/utils_paperspace')
sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/secrets')
from secret import PROJECT_NAME
from manage_workflow import create_or_recup_workflow
from manage_result import clean_result

if __name__ == "__main__":
    #Get the pipeline and run it
    parser = argparse.ArgumentParser()
    parser.add_argument("yamlpath", help="display a square of a given number", type=str)
    args = parser.parse_args()

    id_wf = create_or_recup_workflow("YoloWorkflow", PROJECT_NAME)
    clean_result()
    os.system('gradient workflows run --id ' + id_wf + ' --path ' + args.yamlpath)