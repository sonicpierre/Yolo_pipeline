from game_part.game import create_env
import time
import gym
import torch
import cv2 as cv


env = create_env()
env.step(1)


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

model = torch.hub.load('ultralytics/yolov5', 'custom', path='game_part/pipeline_result/best.onnx') 
while True:

    ret, frame = cap.read()
    results = model(frame)
    df_pd = results.pandas().xyxy[0]

    start_time = time.time()
    passage = False
    while df_pd.shape[0]<0 or time.time() - start_time < 1:
        ret, frame = cap.read()
        results = model(frame)
        df_pd = results.pandas().xyxy[0]

    if df_pd.shape[0]>0:
        if df_pd.loc[0]['name'] == "right":
            env.step(3)
            passage = True
        elif df_pd.loc[0]['name'] == "left":
            env.step(4)
            passage = True
        
    if not passage:
        env.step(2)


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()