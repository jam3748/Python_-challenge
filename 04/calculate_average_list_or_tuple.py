def sum_up_list_or_tuple(list_or_tuple):
    total = 0
    for value in list_or_tuple:
        total += value
    return total

def calculate_average_list_or_tuple(list_or_tuple):
    total = sum_up_list_or_tuple(list_or_tuple)
    length = len(list_or_tuple)
    return total / length
    
sample_list = [10, 50, 100, 300, 400]
sample_tuple = (50, 60, 70, 80, 90, 100)

print(str(sample_list) + "の平均値は" + str(calculate_average_list_or_tuple(sample_list)))
print(str(sample_tuple) + "の平均値は" + str(calculate_average_list_or_tuple(sample_tuple)))
