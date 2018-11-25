def compute(n):
    """记忆化搜索"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if nums[n] == -1:
        nums[n] = compute(n - 1) + compute(n - 2)
    return nums[n]


def compute1(n):
    nums[0] = 0
    nums[1] = 1
    for i in range(2, n + 1):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[n]


if __name__ == '__main__':
    n = 10

    nums = [-1] * (n + 1)

    print(compute1(n))
