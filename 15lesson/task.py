# Traffic Light Decision
# Simulate a traffic light: if the light is "red," print "Stop"; if "yellow," print "Prepare to stop"; if "green," print "Go."
light = input("Write traffic light: ")
def traffic_light():
   if light == 'red':
      print('Stop')
   elif light == 'yellow':
      print("Prepare to stop")
   elif light == 'green':
      print('Go')
   else:
      print("incorrect")
# traffic_light
# Discount Calculation
# Write a program that applies a discount based on purchase amount. If the amount is over $100, apply a 10% discount; otherwise, apply a 5% discount.
discount_amount = int(input("write purchase amount: "))
def discount():
   if discount_amount > 100:
      print(f"You can get 10%: {discount_amount*10/100}")
   else:  
      print(f"You can get 5%: {discount_amount*5/100}")
# discount()

# Password Strength
# Write a function that takes a password and checks if it meets strength criteria: at least 8 characters long, contains both letters and numbers.
def password():
   letter = None
   number = None
   passwords = input("Write your password: ") 
   for i in passwords:
      if i.isalpha():
         letter = True
      elif i.isdigit():
         number = True
      
   if len(passwords) > 8 and letter and number:
      print('Enter')
   else:
      print("None")
password()
# Restaurant Bill Split with Tip Calculator
# Write a program that calculates the bill split with a customizable tip based on service quality. If the service was "excellent," add a 20% tip; for "good," add 15%; and for "average," add 10%. If service was "poor," no tip is added.
bill = 100
result = input("Write the quality: ")
def restaurant():
   if result == "excellent":
      print(bill*120/100)
   elif result == 'good':
      print(bill*115/100)
   elif result == 'average':
      print(bill*110/100)
   else:
      print("None")
restaurant()

# Gym Membership Offer
# Write a program that calculates the membership fee based on age and membership type (basic or premium). Adults (18-60) get 10% off the premium fee. Seniors (60+) get 15% off any membership type, and youths under 18 get a 20% discount on the basic membership only.ded
def membership_offer(): 
   membership = input("Write membership: ")
   age = int(input("Write age: "))

   if age < 60 and age > 18 and membership == 'premium':
      print('get 10% the premium')
   elif age > 60:
      print('get 15% the premium')
   elif age < 18 and membership == "basic":
      print('get 20% the premium')
   else:
      print('None')
membership_offer()


# Grades
grades_dict = {
    "Math": [90, 825, 88],
    "Biology": [28, 82, 85],
    "History": [12, 87, 24],
    "English": [75, 80, 82],
}

def grades_func():
    average_grades = {}
    for subject, grades in grades_dict.items():
        if len(grades) > 0:
            average = sum(grades) / len(grades)
        else:
            average = 0
        average_grades[subject] = average
    print(average_grades)

grades_func()
