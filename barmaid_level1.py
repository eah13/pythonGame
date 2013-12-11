# -*- coding: utf-8 -*-
def player_input(prompt, choice1, choice2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice1;
	print "Choice 2: ", choice2;

print "Welcome to Chapter 1: Breakin' Bad Habits"
print " "
print "As a result of your actions, you’re sent to the dungeon to think about what you've done.\n"
player_input(prompt="What will you do in this dank and lonely cell? Stay dank and lonely or break out?", choice1="stay dank and lonely", choice2="break out")
cellchoices=['stay dank and lonely', 'break out'] #choices dictionary for either leaving cell or staying in the cell 
response= raw_input("What is your choice? ") #raw input for response

if (response).lower() in cellchoices[0]:#User chooses to stay dank
	print "If you wish..."
	import barmaid_level1.py #restarts level
if (response).lower() in cellchoices[1]:#User chooses to break out
	print "Excellent!"

player_input(prompt="...But how will you break out? The way I see it, you have two options. Break down the cell door with your highly reliable beer mug or break the conveniently located window right behind you?", choice1="break down cell door", choice2="break window")
breakoutchoices=['break down cell door', 'break window']#choices dictionary for breaking out
response= raw_input("What is your choice? ")#raw input for breaking out of cell response
if (response).lower() in breakoutchoices[0]:#User chooses to break down cell door
	print "Alas, to no avail."
if (response).lower() in breakoutchoices[1]:#User chooses to break window
	print "Somehow you've managed to break the window quietly enough not to attract any attention from the dungeon guards or your fellow dungeon mates. You escape successfully!"
  		
	player_input(prompt="Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the nearby forest, or back to the palace?", choice1="forest", choice2="palace")
 	freedomchoices=['forest', 'palace'] #choices dictionary for locations
	response= raw_input("What is your choice? ") #raw input for leaving cell and moving to next location
  	if (response).lower() in freedomchoices[0]: #User chooses to go to the forest
  			print "Onward to the next level!" 
  			import barmaid_level2.py #next level loads
  	if (response).lower() in freedomchoices[1]: #User chooses to go back to the palace
  		print "What are you doing?! You can't go back there, the King'll have your head for sure!"
  		player_input(prompt="Do you really want to go back?", choice1="yes", choice2="no")
  		gobackchoices=['yes', 'no'] #choices dictionary for going back to palace or not
  		response= raw_input("What is your choice? ")#raw input for going back to the palace or not 
  		if (response).lower() in gobackchoices[0]: #if the user chooses to go back to the palace...
  			print "The King spots you sneaking across the grounds while he is on one of his evening strolls. He is merciful and sends you back to the dungeon."
  			import barmaid_level1.py #restarts this level
  		if (response).lower() in gobackchoices[1]:
  			print "Good. I knew you were wiser than that."
    			player_input(prompt="Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the nearby forest, or back to the palace?", choice1="forest", choice2="palace")
 			freedomchoices=['forest', 'palace'] #choices dictionary for locations
			response= raw_input("What is your choice? ") #raw input for leaving cell and moving to next location
  			if (response).lower() in freedomchoices[0]: #User chooses to go to the forest
  				print "Onward to the next level!"
  				import barmaid_level2.py #next level loads
    		
