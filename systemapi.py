import os 
import shlex

user_input = input("Enter a parameter: ")
command = f"echo Hellow {user_input}"
safe_command = shlex.quote(command)
print(safe_command)
os.system(safe_command)
#os.system(command)
