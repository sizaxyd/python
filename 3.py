import numpy as np
dim = 7
mid = dim // 2
a = np.zeros([dim, dim])
a[mid, mid] = 1
# print(a)
for i in range(mid):
    # square
    x = (dim - i * 2)
    print('x=',x)
    a[i, i] = x ** 2
    # mirrored value
    mir = dim - i - 1
    a[mir, mir] = a[i, i] - 2*(x - 1)
print("\n", a)
