"""
Class template by JOR
Revision History
06OCT22: Alpha
"""
class MyClass():
 # Constructor, called whenever an instance of the class is created.
 def __init__(self) -> None:
  print("Running Constructor for human class")
  # Take in an argument and assign it to a meaningful attribute name
  self.dob = None
  self.title = None
  self.first_name = None
  self.middle_initial = None
  self.surname = None

# Instantiate the class as MyClass2
MyClass2 = MyClass()
MyClass2.title = "Mr."
MyClass2.first_name = "Leo"
MyClass2.middle_initial = "M"
MyClass2.surname = "O'Callaghan"
# Check the object and type
print(type(MyClass2))
