import numpy as np

def calculate_brightness(img):

    if len(img) <= 0:
        return -1

    # Check row lengths BEFORE np.array()
    if not all(len(r) == len(img[0]) for r in img):
        return -1

    i = np.array(img)

    # Check pixel values
    if np.any(i < 0) or np.any(i > 255):
        return -1

    return np.round(np.mean(i), 2)
