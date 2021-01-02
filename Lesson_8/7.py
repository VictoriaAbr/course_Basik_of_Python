class ComplexInt():
    def __init__(self, x):
        self.x = x

    def __add__(self, cInt):
        return ComplexInt(self.x + cInt.x)

    def __mul__(self, cInt):
        return ComplexInt(self.x * cInt.x)

A = []
for n in (1, 2):
    obj = ComplexInt(n + n * 1j)
    new_element = obj.x
    A.append(new_element)


# def mult_compl(num1, num2):
#     answer = num1 * num2
#     return answer


print(A)

for n in range(len(A)):
    print(A[0] + A[1])
    print(A[0] * A[1])
    # print(sum(A))
    # print(mult_compl(A[0], A[1]))
    break
