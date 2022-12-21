def find_num(number_list: list, number: int)->bool:
# Notes have boolean instead of bool, which returns an error in VSC: NameError: name 'boolean' is not defined
 for iterate_number in number_list:
  if iterate_number == number:
   return True
#  elif iterate_number != number:
#   return False  
  else:
   pass
   
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)
"""
The code iterates through the list of values 1-8 (number_list)
and searches for the value 9 (number)

Because the if statement only returns a Boolean result when the value is matched, the value 9 
being outside the range returns an output of none
Any value outside the range of 1-8 will produce this output

One way to return a value of false would be to modify the if to add an elif statement
The elif evaluates if the value for number is not equal to one of the numbers in the provided range
and returns a value of false if this condition is met 
I've included this code above, commented out  
"""