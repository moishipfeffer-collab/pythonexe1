agents=["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
# section 1
print(agents)
#section 2
print(agents[0:5:4])
#section 3
print(agents[1])
#section 4
print(agents[1:4])
#section 5
agents.append("Foxtrot")
print(agents)
#section 6
agents.insert(2,"zulu")
print(agents)
#section 7
agents.remove("Bravo")
print(agents)