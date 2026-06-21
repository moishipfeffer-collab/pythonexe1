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
     