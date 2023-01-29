# Pollutants_Detection_Yolov7_custom
YoloV7 Visible Pollutants Detection

Custom Yolov7 model trained on 10000 road images for detection of visible pollutants.

Here is the link to prediction in test images:

https://drive.google.com/drive/folders/1d1rs43gzT68giHFmC_GW2ioazm-_jlmu?usp=share_link

Best weights for 70 epochs:

https://drive.google.com/file/d/17sRNWLM5fVTrwe5iyuBUb8O0RltLk0NB/view?usp=share_link

To run detection on your own download the weights and run:

!python detect.py --source "{your_image_location}" --weights best70.pt --save-txt --conf=0.36

Examples:

![00bce25b1d3a3422bb366a12e3e9ac6a](https://user-images.githubusercontent.com/67851367/213874001-8fcf6082-5e97-49f2-8533-5253f4c7d77f.jpg)
![0b4e39c1e1cd3780a8e74403b50aadae](https://user-images.githubusercontent.com/67851367/213874019-9bc312d8-527e-4c88-8c51-c0ce75a3e928.jpg)
![0b7b1672c6bed5a7e2f1a5618787c6f0](https://user-images.githubusercontent.com/67851367/213874030-191764aa-4f44-43d2-8f77-3f66cd2802ae.jpg)
![0dacd86b01d87b56e56415cc51a182ed](https://user-images.githubusercontent.com/67851367/213874076-0f5be953-4378-421f-9245-dd345dcc2776.jpg)
