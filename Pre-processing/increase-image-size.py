from PIL import Image
import os

def resize_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            w, h = image.size
            if w < 200:
                w = 200
                h = h * (200 / w)
            if h < 200:
                h = 200
                w = w * (200 / h)

            image = image.resize((int(w), int(h)))
            image.save(image_path)

    print("Done!")
    
folder_path = "/path/to/your/images"
resize_images(folder_path)
