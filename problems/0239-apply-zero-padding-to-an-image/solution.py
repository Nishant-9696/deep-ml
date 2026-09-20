import numpy as np

def zero_pad_image(img, pad_width):
    img = np.asarray(img)
    # Check valid 2D array
    if img.ndim != 2:
        return -1

    # Check empty dimensions
    if 0 in img.shape:
        return -1

    # Check pad_width
    if pad_width < 0:
        return -1

    # Add zero padding
    padded = np.pad(img, pad_width, mode='constant', constant_values=0)

    return padded.astype(int).tolist()