my_filename = "logfile.txt"
try:
 with open(my_filename, "r") as file_handle:
  print(f"Writing a test line to {my_filename}")
  file_handle.write("Test line")
except IOError as err:
 print(f"IOError was {err}")
except EOFError as err:
 print(f"End of file error was {err}")
except OSError:
 print("OS Error")
except:
 print("General Error")
else:
 print("File created")
finally:
 print("Finishing up!")
 # close not needed because with statement
 # file_handle.close()
# This code cteated an output of a logfile.txt file to C:Users\leooc with contect 'Test line'
# Each subsequent run with open command set as 'a' appends the string 'Test line' to logfile.txt
# Changing the open command from 'a' to 'w' causes the file to be overwritten with 'Test line'
# Changing to 'rw' shows the same behaviour as 'w'
# Changing to 'r' gives an error: "IOError was not writable"

