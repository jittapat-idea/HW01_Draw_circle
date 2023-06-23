import cv2
import numpy as np

def draw_circle(image, center_x, center_y, radius):
    height, width = image.shape[:2]
    for y in range(height):
        for x in range(width):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                image[y, x] = (255, 255, 255)

# สร้างภาพ
image = np.zeros((200, 300, 3), dtype=np.uint8)

# กำหนดพิกัดและขนาดของวงกลม
center_x = 155
center_y = 100
radius = 50

# วาดวงกลมสีขาวบนภาพ
draw_circle(image, center_x, center_y, radius)

# แสดงภาพ
cv2.imshow("Circle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()