from config import LABELS

def create_labmap(dest_dir:str, dico_lab:dict):
    """
    Permet la création d'une labelmap
    """

    labels = dico_lab
    with open(dest_dir, 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')


if __name__=="__main__":
    create_labmap("/outputs/tfrecordsmythumb/labelmap.pbtxt", LABELS)