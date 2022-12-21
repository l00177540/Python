iterable_variable = [1,2,3,4,5,6]
total = 0
for item in iterable_variable:
 total = total + item
print(total)
# Indenting the print statement above casues an indentation error 
# "IndentationError: unexpected indent"
# as the line is assumed to be included in the 'for' statement
