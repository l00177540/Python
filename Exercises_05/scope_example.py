my_string = "global"
def my_function():
 my_string = "enclosing"
 def nested_function():
  my_string = "local"
  print(my_string)
 nested_function()
 return my_string
# Print the variable my_string
print(my_string)
# Print the output of the function, my_function
print(my_function())
# Output is :
# global
# local
# enclosing
# The order is because the nested function executes before the regular function