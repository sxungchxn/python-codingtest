my_dict = {'c': 3, 'a': 1, 'b': 2, 'e': 1, 'd': 2}

sorted_dict = sorted(my_dict.items())  # 오름차순으로 정렬된 tuple들의 list를 반환
print(sorted_dict)


# my_dict의 value를 기준으로 정렬
sorted_dict = sorted(my_dict.items(), key=lambda item: item[1])

print(sorted_dict)
