import os

BATCH = 8
RESIZE = 640
EPOCHS = 100
WORKERS = 24
DATA_SPECIFICATION = "/inputs/repo/training_part_yolo/yolo_specification/thumb.yaml"
HYPERPARAMETERS = "/inputs/repo/training_part_yolo/yolo_specification/hyp.scratch.yaml"
WEIGHTS = "yolov5s.pt"
MODEL_SPECIFICAION = "yolov5s.yaml"
RESULT_FORLDER = "thumb"


def run_yolo():

    initial = "python3 train.py"
    resizing = "--img " + str(RESIZE)
    config_model = "--cfg " + MODEL_SPECIFICAION
    hyperparam = "--hyp " + HYPERPARAMETERS
    batch = "--batch " + str(BATCH)
    epch = "--epochs " + str(EPOCHS)
    data = "--data " + DATA_SPECIFICATION
    weight = "--weights " + WEIGHTS
    workers = "--workers " + str(WORKERS)
    result = "--name " + RESULT_FORLDER


    os.system(" ".join([initial, resizing, config_model, hyperparam, batch, epch, data, weight, workers, result]))


if __name__ == "__main__":
    run_yolo()