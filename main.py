print("Welcome to the Body Mass Index (BMI) Calculator\n")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/(height**2))

if BMI > 18.5:
    if BMI <= 35:
        if BMI <= 30:
            if BMI <= 25:
              print("Your BMI is " + BMI + ", you have a normal weight.")
            else: print("Your BMI is " + BMI + ", you are slightly overweight.")  
        else:
            print("Your BMI is " + BMI + ", you are obese.")
    else:
        print("Your BMI is " + BMI + ", you are clinicaly obese.")
else:
    print("Your BMI is " + BMI + ", you are underweight.")                    