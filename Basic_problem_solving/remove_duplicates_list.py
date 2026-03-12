def remove_duplicates(lst):
    unique_list=[]
    for element in lst:

        if element not in unique_list:
            unique_list.append(element)


    return unique_list
lst=[1,2,3,4,5,6]
print(remove_duplicates(lst))
