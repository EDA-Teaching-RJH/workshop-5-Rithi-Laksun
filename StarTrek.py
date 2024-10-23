import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}") 
		exit() 
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew 
	while ship != 0:
		print("Current status:", ship["systems"]["resources"]["crew"])
def get_user_action(): 
# TODO: Implement function to get and return user's chosen action 
	global action
	action = int(input("Choose a number from 1-4 to do an action: "))
def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 
	turn += 1
	def missions(mission_type): 
		match mission_type:
			case "Exploration":
				crew_member = "Troi"
				ship["systems"]["engines"] = 85
				ship["resources"]["energy"] = 855
				score += 2
				print("score:", score)
				print(crew_member,"is on this mission",(ship["crew"]["Troi"]))
				return "A lot of engines and power was used",(ship["systems"]["engines"]), (ship["resources"]["energy"])
			case "Diplomacy":
				crew_member = "Worf"
				ship["systems"]["engines"] = 80
				ship["systems"]["sensors"] -= 20
				ship["resources"]["energy"] = 900
				score += 3
				print("score:", score)
				print(crew_member,"are on this mission",(ship["crew"]["Worf"]))
				return "A lot of engines,sensors and power was used",(ship["systems"]["engines"]["sensors"]), (ship["resources"]["energy"])
			case "Combat":
				crew_member = "Picard","Data"
				ship["systems"]["engines"] = 65
				ship["systems"]["weapons"]["shields"] -= 30
				ship["resources"]["energy"]= 665
				ship["resources"]["torpedoes"] = 4
				score += 3
				print("score:", score)
				print(crew_member,"are on this mission",(ship["crew"]["Picard"]["Data"]))
				return "A lot of engines,weapons,shields and power was used",(ship["systems"]["engines"]["weapons"]["shields"]), (ship["resources"]["energy"]),(ship["resources"]["torpedoes"])
			case "Rescue":
				crew_member = "La Forge","Riker"
				ship["systems"]["engines"] = 75
				ship["systems"]["shields"]["sensors"] -= 30
				ship["resources"]["energy"] = 700
				score += 2
				print("score:", score)
				print(crew_member,"are on this mission",(ship["crew"]["La Forge"]["Riker"]))
				return "A lot of engines, shields, sensors and power was used",(ship["systems"]["shields"]["sensors"]), (ship["resources"]["energy"])
			case "Scientific Research":
				crew_member = "Crusher"
				ship["systems"]["engines"]["sensors"] = 85
				ship["resources"]["energy"] = 855
				score += 2
				print("score:", score)
				print(crew_member,"is on this mission"),(ship["crew"]["Crusher"])
				return "A lot of engines and power was used",(ship["systems"]["engines"]["sensors"]), (ship["resources"]["energy"])
		missions()

def repair_system(): 
# TODO: Implement system repair functionality
	print("WARNING: there are damages to your ship!")
	ship["systems"]["engines"] -= 20
	ship["systems"]["shields"] -= 25
	ship["systems"]["sensors"] +=25
	ship["resources"]["energy"] -=150
	print("You have less engines and shield due to damage. However now you added more sensors for safety.")
	print("Engines left: ",(ship["systems"]["engines"]))
	print("Shields left: ",(ship["systems"]["shields"]))
	print("Sensors on ship: ", (ship["systems"]["sensors"]))
 
def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 
	ship["crew"]["Wesley"] = "Acting Ensign"
	print("Wesley has been added to the crew!")
def handle_random_event():
# TODO: Implement random events that can occur during the simulation 
	print("You're ship is getting attacked!")
	choose = input("Do you want to leave or fight: ").casefold()
	if choose == "leave":
		print("You escaped but there are slight damages.")
		score -= 1
	elif choose == "fight":
		print("You won! But there are damages.")
		score += 1
		ship["systems"]["weapons"] -=12
	else:
		print("Invalid response.")
		pass

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 
# TODO: Implement resource replenishment logic 


main()
