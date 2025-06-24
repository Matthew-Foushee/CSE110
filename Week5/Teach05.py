percent = input("What is your percentage grade? ")

letter = "F"

lastdiget = int(percent[1])
percent = int(percent)

if(percent >= 90):
  letter = "A"
elif(percent >= 80):
  letter = "B"
elif(percent >= 70):
  letter = "C"
elif(percent >= 60):
  letter = "D"
 
if(percent >= 60 and percent < 97):
  if(lastdiget <= 3):
    letter += "-"
  elif(lastdiget > 7):
    letter += "+"

print(f"you have the letter grade of {letter}")
