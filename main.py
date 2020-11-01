import cv2
import numpy as np

width, height = 600, 600

base_color = (255, 255, 255)

if __name__ == '__main__':
    white_noise = np.random.standard_normal(size=width * height)

    image = np.full((height, width, 3), base_color, dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            t = white_noise[i * width + j]
            if t < 0:
                a = base_color[0] + t
                image[i][j] = (a, a, a)
    
    image = cv2.GaussianBlur(image, (5, 5), 0)

    cv2.imwrite('avatar.png', image)
