def getValidatedInput(message, errmessage, validator):
  while True:
    validated = validator(input(message))

    if validated != None:
      return validated
    if validated == None:
      print(f"\033[91m{errmessage}\033[00m")

def positiveIntValidator(value):
  try:
    validated = int(value)

    if validated < 0:
      return None
    
    return validated
  except:
    return None

def yesOrNoValidator(value):
  strValue = str(value).lower()

  if strValue == "y" or strValue == "yes":
    return True
  if strValue == "n" or strValue == "no":
    return False
  
  print("invalid")
  return None