import os
import shutil

def clean_result():
    """
    Supprime l'ancien jeux de résultats
    """

    if os.path.exists("pipeline_result"):
        shutil.rmtree("pipeline_result")

    os.mkdir("pipeline_result")