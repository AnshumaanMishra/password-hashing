from helper import validPassword, validUsername, generateHash

def register():
  try:
    file1 = open("./data.txt", "r")
    data = file1.read()
    file1.close()
  except FileNotFoundError:
    data = ''

  file1 = open("./data.txt", "a")
  username = input("Enter your username(at Least 8 characters): ")
  while (not validUsername(username)):
    username = input("Username must have at least 8 characters: ")
  print("Your Password must:\n\t1. Have at Least 8 characters\n\t2. Have no special character\n\t3. Have at least one uppercase character\n\t4. Have at least one lowercase character\n\t5. Have at least one digit")
  password = input("Enter your password: ")
  while (not validPassword(password)):
    print("Invalid password")
    password = input("Enter your password: ")
  key = generateHash(username, 24)
  if(data.find(key + "\n") >= 0 or data.startswith(key)):
    print("User already Exists")
    file1.close()
    register()
  else:
    data = key + generateHash(password, 40) + "\n"
    file1.write(data)
    print("Successfully Registered")
    file1.close()