print("Welcome to the Body Mass Index (BMI) Calculator\n")

system = input("Which system would you like to use?\n Type 'i' for Imperial (pounds/ inches) or 'm' for metric: ")


if system == "m" or system == "M":
  height = float(input("enter your height in m: "))
  weight = float(input("enter your weight in kg: "))
  BMI = round(weight/(height**2))
  if BMI > 18.5:
    if BMI <= 35:
        if BMI <= 30:
            if BMI <= 25:
              print(f"Your BMI is {BMI}, you have a normal weight.")
            else: print(f"Your BMI is {BMI}, you are slightly overweight.")  
        else:
            print(f"Your BMI is {BMI}, you are obese.")
    else:
        print(f"Your BMI is {BMI}, you are clinicaly obese.")
  else:
    print(f"Your BMI is {BMI}, you are underweight.")
elif system == "i" or system == "I":
  height = float(input("enter your height in inches: "))
  weight = float(input("enter your weight in lbs: "))
  BMI = round((weight/(height**2))*703)
  if BMI > 18.5:
    if BMI <= 35:
        if BMI <= 30:
            if BMI <= 25:
              print(f"Your BMI is {BMI}, you have a normal weight.")
            else: print(f"Your BMI is {BMI}, you are slightly overweight.")  
        else:
            print(f"Your BMI is {BMI}, you are obese.")
    else:
        print(f"Your BMI is {BMI}, you are clinicaly obese.")
  else:
    print(f"Your BMI is {BMI}, you are underweight.")
else:
   system = input("Please enter either 'i' for Imperial or 'm' for Metric")                    