"""
Class template by JOR
Revision History
06OCT22: Alpha
"""

# Define a class object attribute, it will be the same for any instance of the class
class_object_attribute1 = 6378137
class_object_attribute2 = 6356752

class MyTemplate():
 # Constructor, called whenever an instance of the class is created.
 def __init__(class_object_attribute1: int, class_object_attribute2: int) -> None:
  print("Constructor ran")

# Instantiate the class
my_object = MyTemplate("john", True)

# Check the object and typeprint(type(my_object))
print(my_object.class_object_attribute1, my_object. class_object_attribute2)
