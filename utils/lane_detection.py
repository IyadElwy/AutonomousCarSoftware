import numpy as np
import cv2


# Helper Functions

def canny(image, t1=50, t2=150):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, t1, t2)
    return canny


def hugh_lines(image):
    lines = cv2.HoughLinesP(canny(image), 2, np.pi / 180, 50, np.array([]),
                            minLineLength=2, maxLineGap=15)
    line_image = display_lines(image, lines)
    return line_image


def sharpen_image(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened


def cut_lane_region(image):
    return image[150:, :, :]


def convert_to_numpy_array(image):
    return np.array(image)


def convert_to_pil_image(image):
    return Image.fromarray(image)


# for visualization
def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)

    return line_image


def process_image(image):
    lines = cv2.HoughLinesP(canny(image), 2, np.pi / 180, 50, np.array([]),
                            minLineLength=2, maxLineGap=15)
    line_image = display_lines(image, lines)
    combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return combo_image
