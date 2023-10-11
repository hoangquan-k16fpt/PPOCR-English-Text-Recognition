from paddleocr import PaddleOCR
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

class Inference():
    def __init__ (self) -> None:
        pass

    def infer(self, image_path):

        custom_ocr=PaddleOCR(use_angle_cls=True,
                            rec_model_dir="recognition_infer_pdmodel_acc92",
                            det_model_dir="detection_infer_pdmodel_hmean0.80\\Student1",
                            rec_char_dict_path="PaddleOCR\\ppocr\\utils\\en_dict.txt",
                            use_gpu=True)

        ocr = PaddleOCR(use_angle_cls=True, lang="en")

        results_folder = 'Result'

        image = cv2.imread(image_path)
        height, width, channels = image.shape
        new_image = 225 * np.ones((height, width, 3), dtype=np.uint8)

        results = custom_ocr.ocr(image)

        for (bbox, text) in results:
            # print(text[0])
            points = np.array(bbox, dtype=np.int32)
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))
            # Vẽ hộp giữ quanh văn bản nhận diện
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(new_image, text[0], (top_left[0], top_left[1]), cv2.FONT_HERSHEY_COMPLEX, height/3333, (0, 0, 0), 1)
        
        image_name = os.path.basename(image_path)
        output_image_bbox = f'img_{image_name}'
        output_image_text = f'txt_{image_name}'

        output_bbox_path = os.path.join(results_folder, output_image_bbox)
        output_text_path = os.path.join(results_folder, output_image_text)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        cv2.imwrite(output_bbox_path, image_rgb)
        cv2.imwrite(output_text_path, new_image)

        new_width = width-100
        new_height = height-200

        resized_image = cv2.resize(image, (new_width, new_height))
        image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
        resized_new_image = cv2.resize(new_image, (new_width, new_height))

        cv2.imshow('Image with Bounding Box', image_rgb)
        cv2.imshow('text', resized_new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        
if __name__ == '__main__':

    inference = Inference()

    inference.infer("1_Text Extraction\\1_Text Detection\\data1\\images\\20221022_000000.jpg")