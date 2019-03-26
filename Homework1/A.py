def get_ints():
    return [int(x) for x in input().split(' ')]

ints = get_ints()
print(ints[0] + ints[1])