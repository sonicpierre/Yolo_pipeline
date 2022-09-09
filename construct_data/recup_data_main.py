import get_data as dd
import config as conf
import shutil
import sys
from glob import glob
import os

sys.path.insert(1, '/home/virgaux/Paperspace/Worflows/Yolo_pipeline/utils_paperspace')
from manage_database import dataset_exist, define_dataset, define_version_upload, visualise

if __name__=="__main__":
    #Collect data with the camera
    dd.capture_img()


    if len(glob('*.png')) == len(os.listdir(conf.IMAGES_PATH_CAMERA))/2:

        # Penser à donner un nom de dossier à la fonction si ce n'est pas la première fois qu'on l'utilise
        dd.partition_data()
        shutil.rmtree(conf.IMAGES_PATH_CAMERA)

        #Vérifier par test unitaire que les données sont bien labellisé comme il faut
        #dd.test_data()


        # Permet de coller 2 dossiers de prise de données
        dd.translat_to_dir("Thumb_v1", "Thumb_v2", "Thumb")

        if not dataset_exist(conf.PAPERSPACE_DATA_NAME):
            id_data = define_dataset(conf.PAPERSPACE_DATA_NAME)
            id_version = define_version_upload(conf.PRINCIPAL_FOLDER)
            visualise(id_data, id_version)
        else:
            print("Dataset already exist")
    
    else :
        #Command labelImg to lunch image labelling
        print("Please label your dataset")