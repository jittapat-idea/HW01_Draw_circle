
import cv2
import numpy as np

def draw_circle(image, center_x, center_y, radius, color):
    x = 0
    y = radius
    d = 3 - 2 * radius

    while x <= y:
        draw_circle_points(image, center_x, center_y, x, y, color)

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

def draw_circle_points(image, center_x, center_y, x, y, color):
    draw_pixel(image, center_x + x, center_y + y, color)
    draw_pixel(image, center_x - x, center_y + y, color)
    draw_pixel(image, center_x + x, center_y - y, color)
    draw_pixel(image, center_x - x, center_y - y, color)
    draw_pixel(image, center_x + y, center_y + x, color)
    draw_pixel(image, center_x - y, center_y + x, color)
    draw_pixel(image, center_x + y, center_y - x, color)
    draw_pixel(image, center_x - y, center_y - x, color)

def draw_pixel(image, x, y, color):
    height, width = image.shape[:2]
    if x >= 0 and x < width and y >= 0 and y < height:
        image[y, x] = color

# สร้างภาพ
image = np.zeros((200, 300), dtype=np.uint8)

# กำหนดพิกัดและขนาดของวงกลม
center_x = 150
center_y = 100
radius = 50

center_x1 = 100
center_y1 = 200
radius1 = 50

# วาดวงกลมบนภาพ
draw_circle(image, center_x, center_y, radius, 255)
draw_circle(image, center_x1, center_y1, radius1, 255)

# แสดงภาพ
cv2.imshow("Circle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()