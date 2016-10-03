import numpy as np
dim = 101
mid = dim // 2
# a = np.zeros([dim, dim])
# a[mid, mid] = 1
# print(a)
# for i in range(mid):
#     # square
#     x = (dim - i * 2)
#     a[i, i] = x ** 2
#     # mirrored value
#     mir = dim - i - 1
#     a[mir, mir] = a[i, i] - 2*(x - 1)
# print("\n", a)

b = np.zeros([dim])
b[mid] = 1
# print('b=', b)
for i in range(mid):
    x = dim - i*2
    b[i] = x ** 2
    mir = dim - i - 1
    b[mir] = b[i] - 2*(x-1)
print("sum_b=", sum(b))
