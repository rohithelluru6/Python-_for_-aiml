def square_even(lst):
  result=[]
  for num in lst:
    if num%2==0:
      result.append(num**2)
    
  return result
print(square_even([1,2,3,4,5,6,7,8,9]))
