import cv2 # Import opencv
import uuid # Import uuid
import os # Import Operating System
import time # Import time
import config as conf
from sklearn.model_selection import train_test_split
import shutil

def check_create_arbo(name_image_path:str)->None:
    """
    Check if the dir arborescence is here and construct it else

    labels : List of differents object to detect
    """

    if not os.path.exists(name_image_path):
        os.makedirs(name_image_path)


def capture_img(name=None, idx_cam=0)->int:
    """
    Connect to camera and capture data of different labels

    idx_cam : The idx of the camera try -1 if it doesn't work
    """

    # Allow to name differently the folder that will be created
    if name is None:
        check_create_arbo(name_image_path=conf.IMAGES_PATH_CAMERA)
    else:
        check_create_arbo(name_image_path=name)

    cap = cv2.VideoCapture(idx_cam)
    if not cap.isOpened():
        print("Cannot open camera")
        return 1

    for label in conf.labels:
        print(label)
        number = 0
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                cap.release()
                return 1
            
            imgname = os.path.join(conf.IMAGES_PATH_CAMERA, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imgname, frame)
            cv2.imshow('frame', frame)
            time.sleep(2)

            if cv2.waitKey(1) == ord('q') or number == conf.number_imgs:
                break

            number+=1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0


def move_files_to_folder(list_of_files, destination_folder):
    """
    Utility function to move images 
    """

    def move_file(list_files):

        for f in list_files:
            try:

                shutil.move(f, destination_folder)
            except:
                print(f)
                assert False

    if type(list_of_files) != list:
        list_files = os.listdir(list_of_files)
        move_file([list_files + "/" + i for i in os.listdir(list_files)])

    else:
        move_file(list_of_files)



def create_final_architecture(name_dir=conf.PRINCIPAL_FOLDER) -> None:
    """
    Create the final architecture
    """
    if not os.path.exists(name_dir):
        os.makedirs(os.path.join(name_dir,"images/train"))
        os.makedirs(os.path.join(name_dir,"images/val"))
        os.makedirs(os.path.join(name_dir,"images/test"))
        os.makedirs(os.path.join(name_dir,"labels/train"))
        os.makedirs(os.path.join(name_dir,"labels/val"))
        os.makedirs(os.path.join(name_dir,"labels/test"))

def move_dir(dir_1:str, name:str)->None:
    """
    Concatenate the data in one folder
    """

    # Move the splits into their folders
    move_files_to_folder(os.path.join(dir_1, "images/train"), os.path.join(name, "images/train"))
    move_files_to_folder(os.path.join(dir_1, "images/val"), os.path.join(name, "images/val"))
    move_files_to_folder(os.path.join(dir_1, "images/test"), os.path.join(name, "images/test"))
    move_files_to_folder(os.path.join(dir_1, "labels/train"), os.path.join(name, "labels/train"))
    move_files_to_folder(os.path.join(dir_1, "labels/val"), os.path.join(name, "labels/val"))
    move_files_to_folder(os.path.join(dir_1, "labels/test"), os.path.join(name, "labels/test"))
    

def translat_to_dir(dir_1:str, dir_2:str, name_concat_dir:str)->None:
    """
    Concat the data from two folders to another
    """

    create_final_architecture(name_concat_dir)
    move_dir(dir_1, name_concat_dir)
    move_dir(dir_2, name_concat_dir)


def partition_data(name=None)->None:
    """
    Partition the data in train and test
    """

    # Create the architecture to store the data
    if name is None:
        create_final_architecture()
    else:
        create_final_architecture(name)

    # Read images and annotations
    images = [os.path.join(conf.IMAGES_PATH_CAMERA, x) for x in os.listdir(conf.IMAGES_PATH_CAMERA) if x[-3:] == "jpg"]
    annotations = [os.path.join(conf.IMAGES_PATH_CAMERA, x) for x in os.listdir(conf.IMAGES_PATH_CAMERA) if x[-3:] == "txt" and x!="classes.txt"]

    # Sort images and annotations
    images.sort()
    annotations.sort()

    # Split the dataset into train-valid-test splits 
    train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.2, random_state = 1)
    val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)

    # Move the splits into their folders
    move_files_to_folder(train_images, os.path.join(conf.PRINCIPAL_FOLDER, "images/train"))
    move_files_to_folder(val_images, os.path.join(conf.PRINCIPAL_FOLDER, "images/val"))
    move_files_to_folder(test_images, os.path.join(conf.PRINCIPAL_FOLDER, "images/test"))
    move_files_to_folder(train_annotations, os.path.join(conf.PRINCIPAL_FOLDER, "labels/train"))
    move_files_to_folder(val_annotations, os.path.join(conf.PRINCIPAL_FOLDER, "labels/val"))
    move_files_to_folder(test_annotations, os.path.join(conf.PRINCIPAL_FOLDER, "labels/test"))