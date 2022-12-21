# Define a string to iterate over
for this_letter in "Leo O'Callaghan":
 # Specify which letter to test for
 if this_letter == "L":
    # Found the test letter
    print(f"Woo hoo, found a {this_letter}!")
    # Exit the current loop
    break
else:
 # Didn't find the test letter
 print(f"Aww man, I didn't want a {this_letter}!")
