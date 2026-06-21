where_to_go=input("where do you want to go? \n 1) forest \n 2) cave \n 3) river \n choose: ")
if where_to_go == "forest":
 hide_or_walk=input("do you want to hide or walk? ")
 if hide_or_walk == "hide":
  print("You hide behind a tree")
 elif hide_or_walk == "walk":
  print("You find a sleeping wolf")
 else:
  print("Invalid forest action")