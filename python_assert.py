def average(list):
    assert len(list) != 0
    answer = sum(list)/len(list)
    return answer

n= average([3, 5, 6,8])
print(n)