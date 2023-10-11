import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from paddleocr import PaddleOCR

class Inference:
    def __init__(self, app):
        self.app = app
        self.result_label = tk.Label(self.app.root, text="")
        self.result_label.pack()

    def infer(self, image_path):
        custom_ocr = PaddleOCR(use_angle_cls=True,
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
            points = np.array(bbox, dtype=np.int32)
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(new_image, text[0], (top_left[0], top_left[1]), cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)

        image_name = os.path.basename(image_path)
        output_image_bbox = f'img_{image_name}'
        output_image_text = f'txt_{image_name}'

        output_bbox_path = os.path.join(results_folder, output_image_bbox)
        output_text_path = os.path.join(results_folder, output_image_text)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        cv2.imwrite(output_bbox_path, image_rgb)
        cv2.imwrite(output_text_path, new_image)


        cv2.imshow('Image with Bounding Box', image_rgb)
        cv2.imshow('text', new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Hiển thị kết quả lên giao diện
        self.result_label.config(text="OCR hoàn thành.")

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR App")
        self.root.geometry("500x750")  # Đặt kích thước cửa sổ

        self.inference = Inference(self)

        self.image_path = None

        self.select_image_button = tk.Button(root, text="Chọn ảnh", command=self.load_image)
        self.select_image_button.pack(pady=20)  # Thêm khoảng cách từ nút chọn ảnh đến cạnh trên

        self.start_ocr_button = tk.Button(root, text="Bắt đầu OCR", command=self.run_ocr)
        self.start_ocr_button.pack(pady=10)  # Thêm khoảng cách từ nút bắt đầu OCR đến cạnh trên

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=20, pady=20, expand=True)  # Thêm khoảng cách từ ảnh đến các cạnh và set expand=True

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            image = Image.open(self.image_path)
            # Lấy kích thước của cửa sổ
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            # Thay đổi kích thước ảnh để phù hợp với kích thước cửa sổ
            image = image.resize((window_width - 40, window_height - 100), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            self.image_label.config(image=image)
            self.image_label.image = image

    def run_ocr(self):
        if self.image_path:
            self.inference.infer(self.image_path)
        else:
            self.result_label.config(text="Hãy chọn ảnh trước khi bắt đầu OCR.")

if __name__ == '__main__':
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
