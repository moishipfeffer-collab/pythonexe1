agent_name="shalom"
mission_code=315436
distens_to_target_in_km=2
mission_active_status=True
print(f"the agent name is, {agent_name}, the mission code is {mission_code}")
print("distens to target in km is", (distens_to_target_in_km))
print("the active status is", mission_active_status)
print (type(agent_name))
print (type(mission_code))
print (type(distens_to_target_in_km))
print (type (mission_active_status))
travel_distance_in_km=20
print ("full distance for a trip from base to target and back in km is", travel_distance_in_km)
fuel_usage=3
fuel_for_travel=fuel_usage * travel_distance_in_km
print("liter fuel for km is", fuel_usage)
print("liter fuel for travel is", fuel_for_travel)
total_fuel=95
fuel_remains_after_mission=total_fuel - fuel_for_travel
print("the fuel that remains after tne mission is", fuel_remains_after_mission)
countdown_conversion=(int(input("how much secons to the mission?")))
print("in minutes it is", countdown_conversion / 60)
print ("in hours it is", countdown_conversion / 60 / 60)
print ("in seconds it is", countdown_conversion)
