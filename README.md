# PPOCR-English-Text-Recognition

#### This is an English text recognition project using PaddleOCR of team 3.
The current source code includes 3 folders:
- [./App](App): the code folder that uses tkinter (GUI interface) to infer the results of the OCR model.
- [./Inference](Inference): the main code directory is used to infer the results of the ocr model. If you use this code to infer the results, you need to edit this [line](Inference/infer_demo.py#L69) with an absolute path to the image you need to OCR.
- [./Pre-processing](Pre-processing): folder containing code for preprocessing input data (image containing text). This folder contains 2 files with the .py extension. The [increase-image-size.py](Pre-processing/increase-image-size.py) is used to change the size of the image, and the [resolution.py](Pre-processing/resolution.py) is used to change the resolution of the image.
- [./Training](Training): folder contains the files needed to retrain the PaddleOCR model, these files include files from [PaddlePaddle's github](https://github.com/PaddlePaddle/PaddleOCR) as well as files we have created and edited. For the smoothest use and to limit unwanted errors, we recommend using this existing folder. If you are someone who likes to learn more about how PaddleOCR works and the original files, you can visit the github page; we recommend that you should use PaddleOCR's Chinese github for the most in-depth and general overview.

Details current source in [./Training](Training) folder:
- [training-model.ipynb](Training/training-model.ipynb): the main source code file of the project, including training data, evaluation and inference code. Also includes code explanation. This is the final training code that we used and is also which that gives the best results and is the model we use in practice up to now.

##### We will update more source codes soon...
