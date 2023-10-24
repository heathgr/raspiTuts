def validatedInput(message, errMessage, validator):
  while True:
    userInput = input(message)
    validatedInput = validator(userInput)

    if not validatedInput:
      print(f"\033[91m{errMessage}\033[00m")
    if validatedInput:
      return validatedInput

def numberOfGradesValidator(value):
  validatedValue = None
  
  try:
    validatedValue = int(value)
  except:
    return None
  
  if validatedValue < 1:
    return None

  return validatedValue

def gradeValueValidator(value):
  validatedValue = None

  try:
    validatedValue = float(value)
  except:
    return None
  
  if validatedValue < 0:
    return None
  if validatedValue > 100:
    return None
  
  return validatedValue

numberOfGrades = validatedInput(
  "How many grades do you want to enter? ",
  "Enter an integer with value greater than 1.",
  numberOfGradesValidator
)

grades = []

for i in range(0, numberOfGrades):
  newGrade = validatedInput(
    f"Enter the value of grade number {i + 1}: ",
    "Grade must be a number between 0 and 100.",
    gradeValueValidator
  )
  grades.append(newGrade)

print(f"The average grade is {sum(grades) / len(grades)}.")


