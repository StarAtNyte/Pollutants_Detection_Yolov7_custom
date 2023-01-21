import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import torch

st.title('Detect Pollutants from an image.')
import os

import yolov7

# load pretrained or custom model
model = torch.load('best50.pt')


# set image
uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    result = model(uploaded_file)
    predictions = result.pred[0]
    boxes = predictions[:, :4] # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    result.show()
