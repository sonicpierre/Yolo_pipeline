def create_labmap(dest_dir:str, dico_lab:dict):

    labels = dico_lab

    with open(dest_dir, 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')


if __name__=="__main__":
    dico = {'name':'left', 'id':1}, {'name':'right', 'id':2}
    create_labmap("/outputs/tfrecordsmythumb/labelmap.pbtxt", dico)