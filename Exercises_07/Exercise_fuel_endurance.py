# Exercise for Walkthrough 7

def diesel_generator_calculator():

 while True:
  try:
   fuel = input("Enter the amount of fuel remaining: ")
   fuel = int(fuel)
   consumption = input("Enter  the fuel consumption: ")
   consumption = int(consumption)
   if consumption == 0:
    raise Exception("Value for consumption must be non-zero")  
   else:    
    endurance = fuel/consumption
    endurance = int(endurance)
    print("Endurance in minutes is:", endurance,)
  except:
   print("Error: Please enter an integer value")
   continue
diesel_generator_calculator()
