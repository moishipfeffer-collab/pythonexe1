#section 1
given_age=int(input("what is your age? "))
if given_age > 17:
    print("can enter")
else:
    print("Cannot enter")
#section 2
temperature = 38.2
if temperature > 37.5:
    print("High temperature")
else:
    print("Normal temperature")
#section 3
given_number=int(input("give a number "))
if given_number % 2 == 0:
    print("Even number")
else:
    print("Odd number")  
#section 4
battery = 15 
is_charging = True
if battery < 20 and is_charging == True:
    print ("Low battery, charging now")
elif battery < 20 and is_charging == False:
    print("Low battery, connect charger")   
else:
    print("Battery OK") 
#section 5
given_password=(input("what is the password? ")) 
password="python123"
if given_password == password:
    print("Access approved")
else:
    print("Access denied") 
        


