class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        matrix = []
        for row in rows:
            matrix.append([int(el) for el in row.split(" ")])

        self.matrix = matrix

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        col = []
        for row in self.matrix:
            col.append(row[index - 1])

        return col
