from helper import generateHash

def login():
  file1 = open("./data.txt", "r")
  data = file1.read()
  file1.close()
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  key = (generateHash(username, 24) + generateHash(password, 40))
  if(data.find(key) >= 0):
    print("Welcome!")
  else:
    print("Invalid Username or Password")
    login()
