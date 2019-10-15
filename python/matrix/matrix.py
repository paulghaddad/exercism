class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = self._parse_matrix_string(matrix_string)
        self.cols = [list(col) for col in zip(*self.rows)]


    def row(self, index):
        return self.rows[index - 1]


    def column(self, index):
        return self.cols[index - 1]


    @staticmethod
    def _parse_matrix_string(matrix):
        return [[int(el) for el in row.split(" ")] for row in matrix.splitlines()]
