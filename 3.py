import numpy as np
dim = 5
mid = dim // 2
a = np.zeros([dim, dim])
a[mid, mid] = 1
# print(a)
for i in range(mid):
    # square
    x = (dim - i * 2) ** 2
    a[i, i] = x
    # mirrored value
    mir = dim - i - 1
    print('mir=', mir)
    a[mir, mir] = x - (mir * 2)
print("\n", a)
