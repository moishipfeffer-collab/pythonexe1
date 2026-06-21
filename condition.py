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
#section 6
score = 72
if score > 89:
    print("Excellent")   
elif score > 74:
    print("good")  
elif score > 59:
    print("pass")
else:
    print("fail")  
#section 7
given_number_1=int(input("give number 1: "))
given_number_2=int(input("give number 2: "))
if given_number_1 > given_number_2:
    print("First is bigger")
elif given_number_1 < given_number_2: 
    print("Second is bigger")
else:
    print ("Equal")  
#sektion 8
fuel = 40 
distance = 30
if fuel - distance > 9: 
    print("Enough fuel with reserve")      
elif fuel - distance > 0:
    print("Enough fuel, low reserve")
else:
    print("Not enough fuel")  
# section 9
given_user_name=input("what is your user name? ")  
if given_user_name:
    print("hello", given_user_name)    
else:
    print("Guest user")
#section 10
hour = 21
if hour < 0 or hour > 23:
    print ("Invalid hour")
elif hour < 12:
    print("Morning") 
elif hour < 18:
    print("Afternoon") 
else:
    print("Evening")           


