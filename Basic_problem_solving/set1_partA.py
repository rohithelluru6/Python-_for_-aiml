def analyze_list(lst):
    sum_val = 0
    even_count = 0
    odd_count = 0
    for num in lst:
        sum_val += num
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    average = sum_val / len(lst)
    return sum_val, average, even_count, odd_count

c=analyze_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(c)
