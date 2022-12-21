def divisible(numerator: int, denominator: int)->bool:
# Notes have boolean instead of bool, which returns an error in VSC: NameError: name 'boolean' is not defined
# First line is defining a function called divisible 
# It accepts 2 integar variables and outputs a Boolean value
 return numerator % denominator == 0
 
print(divisible(30,4))
# A value of 30 is assigned to the numerator and 4 to the denominator
# The calculation is therefore 30 % 4 == 0 (i.e. Is the modulus of the 2 numbers equal to zero
# The output is false as 30 dvided by 4 has a modulus of 7.5
# Values that equate to a modulus of zero will return True. e.g. print(divisible(20,4))
