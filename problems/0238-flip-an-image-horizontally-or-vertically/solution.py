import numpy as np

def flip_image(image, direction):
    image = np.asarray(image)

    # Check direction
    if direction not in ['horizontal', 'vertical']:
        return -1

    # Must be 2D or 3D
    if image.ndim not in [2, 3]:
        return -1

    # Check empty dimensions
    if 0 in image.shape:
        return -1

    if direction == 'horizontal':
        flipped = np.fliplr(image)
    else:
        flipped = np.flipud(image)

    return flipped.tolist()