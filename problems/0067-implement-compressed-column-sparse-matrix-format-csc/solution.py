def compressed_col_sparse_matrix(dense_matrix):

    values = []
    row_idx = []
    col_ptr = [0]

    rows = len(dense_matrix)
    cols = len(dense_matrix[0])

    for j in range(cols):              # column
        for i in range(rows):         # row

            if dense_matrix[i][j] != 0:
                values.append(dense_matrix[i][j])
                row_idx.append(i)

        col_ptr.append(len(values))

    return values, row_idx, col_ptr