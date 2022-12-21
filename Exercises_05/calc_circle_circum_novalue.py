def calculate_circumference(radius):
 """
 Calculate the circumference of a circle based on its radius
 """
 return 2 * 3.142 * radius 
a = calculate_circumference()
print(a)
# Output is error: TypeError: calculate_circumference() missing 1 required positional argument: 'radius'