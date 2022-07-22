from flask import Flask,render_template,Response,request
# import cv2
# import time
from flask import Flask, request, jsonify
import numpy as np


app=Flask(__name__)


# import torch
# import cv2
# import time
# import time
# import numpy as np
# #model = torch.hub.load('ultralytics/yolov5', 'custom',path="yolov5s.onnx",force_reload=True)
# classes = model.names
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print("\n\nDevice Used:",device)
# print("-------------------------------------------")


# def score_frame(frame):
#         """
#         Takes a single frame as input, and scores the frame using yolo5 model.
#         :param frame: input frame in numpy/list/tuple format.
#         :return: Labels and Coordinates of objects detected by model in the frame.
#         """
#         model.to(device)
#         frame = [frame]
#         results = model(frame)
#         labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
#         # print("------------------------------------------------------------")
#         # print(labels)
#         # print("------------------------------------------------------------")
#         return labels, cord


@app.route('/', methods=['GET'])
def predict():
    frame = request.form.get('frame')
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(frame)

    # result=score_frame(frame)

    return jsonify(frame)




if __name__ == '__main__':
    app.run(debug=True)
