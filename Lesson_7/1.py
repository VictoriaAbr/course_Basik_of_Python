
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[5, 2, 8], [6, 1, 2], [0, 7, 5]])
print(matrix_1)
print(('*')*9)
print(matrix_1 + matrix_2)
