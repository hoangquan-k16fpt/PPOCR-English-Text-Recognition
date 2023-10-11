import os
import cv2

def resize_images(input_folder, output_folder, a4_width=2480, a4_height=3508, desired_resolution=1000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.bmp')):
            input_path = os.path.join(input_folder, filename)
            img = cv2.imread(input_path)
            aspect_ratio = img.shape[1] / img.shape[0]

            if aspect_ratio > 1:
                new_height = a4_width / aspect_ratio
                new_size = (int(a4_width), int(new_height))
            else: 
                new_width = a4_height * aspect_ratio
                new_size = (int(new_width), int(a4_height))

            resized_img = cv2.resize(img, new_size)
            resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
            dpi = (desired_resolution, desired_resolution)
            
            cv2.imwrite(
                os.path.join(output_folder, filename),
                cv2.cvtColor(resized_img, cv2.COLOR_RGB2BGR),
                [int(cv2.IMWRITE_JPEG_QUALITY), 100]
            )

    print("Chuẩn hóa kích thước và độ phân giải hoàn tất.")

# Example usage:
input_folder = ""
output_folder = ""
resize_images(input_folder, output_folder)
