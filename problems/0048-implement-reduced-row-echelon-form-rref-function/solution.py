import numpy as np

def rref(matrix):
    A = matrix.astype(float).copy()
    rows, cols = A.shape

    pivot_row = 0

    for col in range(cols):

        # Find a row with non-zero value in this column
        pivot = None

        for row in range(pivot_row, rows):
            if abs(A[row, col]) > 1e-10:
                pivot = row
                break

        # No pivot in this column
        if pivot is None:
            continue

        # Swap pivot row with current row
        A[[pivot_row, pivot]] = A[[pivot, pivot_row]]

        # Make pivot equal to 1
        A[pivot_row] = A[pivot_row] / A[pivot_row, col]

        # Make all other values in pivot column zero
        for row in range(rows):
            if row != pivot_row:
                A[row] = A[row] - A[row, col] * A[pivot_row]

        pivot_row += 1

        # All rows processed
        if pivot_row == rows:
            break

    # Remove tiny floating-point errors
    A[np.abs(A) < 1e-10] = 0

    return A