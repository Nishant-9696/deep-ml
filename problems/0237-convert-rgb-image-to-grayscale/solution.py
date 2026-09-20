import numpy as np

def rgb_to_grayscale(image):
    image = np.asarray(image)
    if image.ndim != 3 or image.shape[2] != 3:
        return -1

    if 0 in image.shape:
        return -1

    if np.any(image < 0) or np.any(image > 255):
        return -1
    
    r=image[:,:,0]
    g=image[:,:,1]
    b=image[:,:,2]
    g= 0.299 * r + 0.587 * g + 0.114 * b
    return np.rint(g).astype(int).tolist()

    