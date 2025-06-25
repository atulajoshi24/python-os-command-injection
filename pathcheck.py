import os


def path_check(input):
  
  root_path = "E:\\Passionpreneour"
  user_path = "E:\\Passionpreneour\\SecurityCourse\\"
  joined_path = os.path.join(user_path, input)

  normalised_joined_path = os.path.realpath(joined_path)

  if normalised_joined_path.startswith(root_path):
    return True
  else:
    return False
    

   
print(path_check("..//..//PassionpreneourPro//sensitive.txt"))
 