import numpy as np

def square_relu(x: np.ndarray) -> dict:
    output = []
    derivative = []

    for value in np.nditer(x):
        if value > 0:
            output.append(float(value * value))
            derivative.append(float(2 * value))
        else:
            output.append(0.0)
            derivative.append(0.0)

    return {
        'output': np.round(np.array(output).reshape(x.shape),2),
        'derivative': np.round(np.array(derivative).reshape(x.shape),2)
    }