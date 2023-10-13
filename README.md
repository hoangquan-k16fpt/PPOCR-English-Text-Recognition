# PPOCR-English-Text-Recognition

#### This is an English text recognition project using PaddleOCR of team 3.
The current source code includes 3 folders:
- [./App](App): the code folder that uses tkinter (GUI interface) to infer the results of the OCR model.
- [./Inference](Inference): the main code directory is used to infer the results of the ocr model. If you use this code to infer the results, you need to edit this [line](Inference/infer_demo.py#L69) with an absolute path to the image you need to OCR.
- [./Pre-processing](Pre-processing): folder containing code for preprocessing input data (image containing text). This folder contains 2 files with the .py extension. The [increase-image-size.py](Pre-processing/increase-image-size.py) is used to change the size of the image, and the [resolution.py](Pre-processing/resolution.py) is used to change the resolution of the image.

##### We will update more source codes soon...
