characters = "19ZFohA8D4rekqRSVLnHK62vYWslOtU5jIfPBJi0mg7cQdEMaxbwzCXuGp3NTy"

def validPassword(password):
  if(len(password) < 8):
    return False
  upper = 0
  lower = 0
  number = 0
  for char in password:
    if(char not in characters):
      return False
    else:
      if(char.isupper()):
        upper += 1
      elif(char.islower()):
        lower += 1
      elif(char.isdigit()):
        number += 1
  if(upper == 0 or lower == 0 or number == 0):
    return False
  return True

def validUsername(username):
  if(len(username) < 8):
    return False
  for char in username:
    if(char not in characters):
      return False
  return True

def getOrd(character, modifier):
  if(character.islower()):
      return ord(character) - ord('a') + modifier + 1
  if(character.isupper()):
      return ord(character) - ord('A') + modifier + 27
  if(character.isdigit()):
      return ord(character) - ord('0') + modifier + 52
  return 0

def getConcat(char1, char2, modifier):
  answer = getOrd(char1, modifier) % len(characters) - getOrd(char2, modifier) % len(characters)
  if(answer < 0):
    answer *= -1
  return characters[answer]

def generateHash(username, Hashlen):
  hash = ''
  iter = 0
  for i in range(Hashlen):
    safeindex = i % len(username)
    hash += getConcat(username[safeindex], username[(safeindex + 1 + iter) % len(username)], getOrd(username[safeindex], iter + safeindex))
    if(safeindex + 1 == len(username)):
      iter += 1
  return hash