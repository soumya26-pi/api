from flask import Flask,render_template,Response,request
# import cv2
# import time
from flask import Flask, request, jsonify
import numpy as np


app=Flask(__name__)



@app.route('/frame', methods=['POST'])
def predict():
    # if request.method=="POST":
    output=request.form.get("frame")
    return jsonify({"frame":str(output)})





if __name__ == '__main__':
    app.run(debug=True)



