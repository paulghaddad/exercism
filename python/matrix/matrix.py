class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self._parse_matrix_string(matrix_string)


    def row(self, index):
        return self.matrix[index - 1]


    def column(self, index):
        return [row[index - 1] for row in self.matrix]


    @staticmethod
    def _parse_matrix_string(matrix_string):
        matrix = []

        for row in matrix_string.split("\n"):
            matrix.append([int(el) for el in row.split(" ")])

        return matrix
