count = 0

for x in range(1, 1000000):
    i_right = x % 1000
    i_left = x // 1000
    i_right_sum = (i_right // 100) + (i_right % 10) + (i_right % 100 // 10)
    i_left_sum = (i_left // 100) + (i_left % 10) + (i_left % 100 // 10)
    if (i_right_sum == i_left_sum):
        print(x)
        count += 1

print(count)

# x = 123456
# i_right = x % 1000
# i_left = x // 1000
# i_right_sum = (i_right // 100) + (i_right % 10) + (i_right % 100 // 10)
# i_left_sum = (i_left // 100) + (i_left % 10) + (i_left % 100 // 10)
# print(i_right)
# print(i_right_sum)
# print(i_left)
# print(i_left_sum)
