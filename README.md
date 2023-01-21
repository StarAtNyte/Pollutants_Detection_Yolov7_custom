# Pollutants_Detection_Yolov7_custom
YoloV7 Visible Pollutants Detection

Custom Yolov7 model trained on 10000 road images for detection of visible pollutants.

Here is the link to the dataset used:
..

Here is the link to prediction in test images:

https://drive.google.com/drive/folders/1d1rs43gzT68giHFmC_GW2ioazm-_jlmu?usp=share_link

Best weights for 70 epochs:

https://drive.google.com/file/d/17sRNWLM5fVTrwe5iyuBUb8O0RltLk0NB/view?usp=share_link

To run detection on your own download the weights and run:

!python detect.py --source "{your_image_location}" --weights best70.pt --save-txt --conf=0.36
