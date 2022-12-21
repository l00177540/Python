def odd_even(number_list: list)->bool:
# Notes have boolean instead of bool, which returns an error in VSC: NameError: name 'boolean' is not defined
 for iterate_number in number_list:
  if iterate_number % 2 == 0:
   return True 
  else:
   return False 
   
result = odd_even([2,4])
# The line above returns a True as even numbers are present in the list
 
#result = odd_even([1,3,5,7])
# The commented out line above returns a false as no even numbers present in the list
print(result) 