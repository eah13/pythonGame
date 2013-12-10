def player_input(prompt, choice1, choice2):
        "this prompts the player with the choices for the game"
        print "Prompt: ", prompt;
        print "Choice 1: ", choice1;
        print "Choice 2: ", choice2;
        
print "Welcome to our Medieval Python RPG!" 
player_input(prompt="Are you going to be a girl or boy in this game?", choice1="girl", choice2="boy")
genderchoices=['girl', 'boy']
response=raw_input("What is your choice?")#Input to ask the user what his or her gender is

if (response).lower() in genderchoices[0]:
  	print " Oh, you're a girl! You are a bar maid with an attitude. After recently being homeless on the streets of Karflooglesville, you are now working for the royal family. In particular, your duty is to serve the king his favorite alcoholic beverages. Today, the King has gotten sick of your beer-serving abilities. For some reason, you are off your game and he insists that the beverage is simply too flat, it tastes unbearable, and the smell is too sweet for his senses." #As a female, this is the backstory that will print out
    	player_input(prompt="Do you speak up or comply?", choice1="speak up", choice2="comply")#Input to ask the user how he/she will answer the king
    	
    	answerchoices=['speak up', 'comply']
    	response= raw_input("What is your choice?") #raw input for response
    	if (response).lower() in answerchoices[0]: #If the user speaks up and stands up to the king...
		print "In return, you inform the King that his breath is unbearable and you are sent to the dungeon. The 		King goes into a rage and send you to solitary confinement."#After speaking up, this is the 					response that will be printed out
		import barmaid_level1.py #After being sent to the dungeon, Level 1 of the Bar Maid's version of the game 		will be imported 
	if (response).lower() in answerchoices[1]: #If the user complies and does not defy the king...
		print "Really? You will let such a defiant moment pass?" #After complying, this is the response that 			will be printed out
		import intro.py #After complying, the user will be forced to restart the "Intro" portion of the game
if (response).lower() in genderchoices[1]:
        print " Oh, a boy I see. So you are a palace scribe who has been working for the King of Karflooglesville for a number of years now. As a young boy, your parents sent you to work for the palace in order to pay for their overdue taxes. The King has grown fond of you, but as of late, the King has been displeased with the notes you've taken because you haven't written enough about him to satisfy his arrogance.\n" #As a male, this is the backstory that will print out
	player_input(prompt="Do you speak up or comply?", choice1="speak up", choice2="comply")#Input to ask the user how he/she will answer the king
    	
    	talkchoices=['speak up', 'comply']
    	response= raw_input("What is your choice?")#raw input for response
	if (response).lower() in talkchoices[0]: #If the user speaks up and stands up to the king...
		print " The King goes into a rage and send you to solitary confinement." #After speaking up, this the 			response that will be printed out
		import scribe_level1.py #After being sent to the dungeon, Level 1 of the Scribe's version of the game 			will be imported
	if (reponse).lower() in talkchoices[1]: #If the user complies and does not defy the king...
		print "Really? You will let such a defiant moment pass?" #After complying, this is the response that 			will be printed out
		import intro.py #After complying, the user will be forced to restart the "Intro" portion of the game

	
	
	


