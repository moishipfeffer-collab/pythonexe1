where_to_go=input("where do you want to go? \n 1) forest \n 2) cave \n 3) river \n choose: ")
if where_to_go == "forest":
 hide_or_walk=input("do you want to hide or walk? ")
 if hide_or_walk == "hide":
  print("You hide behind a tree")
 elif hide_or_walk == "walk":
  print("You find a sleeping wolf")
 else:
  print("Invalid forest action")
elif where_to_go == "cave":
  have_a_torch=input("do you have a torch? ")
  if have_a_torch == "yes":
   left_or_right=input("do you want to go left or right? ")
   if left_or_right == "left":
    print("You find gold") 
   elif left_or_right == "right":
    print ("You find bats")
   else:
    print ("Invalid cave path")
  else:
   print("It is too dark to enter") 
elif where_to_go == "river":
 print("You find a boat")
else:
 print("Unknown place")
 #section 2
 number_1=float(input("give number 1: "))
 number_2=float(input("give number 2: "))
 action=input("choose an action: \n 1) add \n 2) subtract \n 3) multiply \n choose: ")
match action:
  case "add": print(number_1 + number_2)
  case "subtract": print(number_1 - number_2)
  case "multiply": print(number_1 * number_2)
  case _: print("Unknown action")
# section 3
computer_choice = "rock"
rock_paper_scissors=input("what do you want to enter? \n rock. \n paper \n scissors. \n chosse: ")
if rock_paper_scissors == computer_choice:
 print("Draw")
elif rock_paper_scissors == "paper":
 print("You win")
elif rock_paper_scissors == "scissors": 
 print("Computer wins")
elif rock_paper_scissors == "rock":
 print("drow")
else:
 print("Invalid move")
# section 4
correct_pin = 4321 
balance = 500
given_pin=int(input("give a pin code: "))
if given_pin == correct_pin:
 noney=int(input("how much money do you want to withdraw? "))
 if noney > balance:
  print("Not enough money")
 else:
   entering=input("do you want a receipt? ")
   if entering == "yes":
    print("Withdrawal approved with receipt")
   elif entering == "no":
    print("Withdrawal approved without receipt")
   else:
    print("Withdrawal approved")
else:
 print("Wrong PIN")  
 # section 5
club_member=input("are you a club member? ")
if club_member == "yes":
 coupon=input("do you have a coupon? ")
 if coupon == "yes":
  print("Free delivery and 10 discount")
 else:
  print("Free delivery") 
elif club_member == "no":
 print("Delivery costs 15")  
  