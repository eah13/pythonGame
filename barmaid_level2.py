def player_input(prompt, choice1, choice2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice1;
	print "Choice 2: ", choice2;

print "Welcome to Chapter 2: The Forest of Love!" 
print " "
print "You have successfully escaped from your cell! But you are being chased by the palace guards. You run for your life and end up crashing into a handsome lad."
print " "

player_input(prompt="You give him a terrible gash across his thigh.  He is tearing up from the pain.  Will you heal his cut with your magical beer mug or give him an angry look?", choice1="heal cut", choice2="angry look")#this is the first prompt to the user regarding healing

painchoices=['heal cut','angry look'] #choices dictionary for the first prompt

response= raw_input("What is your choice?") #raw input for response

if (response).lower() in painchoices[0]: #User chooses to heal cut
	print "He says thank you and asks why you, the bar maid, is running through the forest. You reply and say that you are running from the palace guards because you defied the king.  He then provides refuge for you in return for you healing him.  As you begin conversing to better know your savior, he tells you of the beast that has been tormenting his village.  He believes that you can do something about the beast since you have magic!  He looks at you with a desperate look."
	player_input(prompt="Will you choose to ignore the story or will you do something about the beast?", choice1="Ignore story", choice2="Beast") #User prompted to ignore story or do something about the beast

	storychoices=['ignore story','beast']

	response= raw_input("What is your choice?") #raw input for response

	if (response).lower() in storychoices[1]: #User chooses to do something about the beast
		print "You proceed to tell him you will do what you can to protect his village.  He exclaims with appreciation and gives you a hug.  He embarassingly thanks you and leads you to the blacksmith to help you fight the beast.  You greet the blacksmith.  The blacksmith grunts, looks you over, and laughs.  He underestimates you and proceeds to say that a lady cannot defeat the village beast.  Your savior persuades the blacksmith that because you have magic, you can defeat the beast."
		player_input(prompt="He reluctantly asks you what you would prefer,suit of armor or spiked hammer?", choice1="Armor", choice2="Hammer") #User prompted to choose armor or sword

		blacksmithchoices=['armor','hammer'] #Dictionary for prompt choices

		response=raw_input('What is your choice?') #raw input for response

		if (response).lower() in blacksmithchoices[0]: #User chooses armor
			print "The blacksmith laughs, creates a suit of armor for you, and you can barely walk.  The blacksmith laughs as you fall to the ground and continues to laugh at your failure.  He bids you good luck and you slowly leave the blacksmith.  You travel to the cave where the beast is located."

			player_input(prompt="Do you enter the cave or do you hesitate?", choice1="Enter", choice2="Hesitate") #User prompted to enter or hesitate at the cave

			cave0choices=['enter','hesitate'] #Dictionary for prompt choices			
			response=raw_input('What is your choice?') #raw input for user
			
			if (response).lower() in cave0choices[0]: #Enter the Cave
				print "You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.  The fireball hits your armor and you get flung backwards.  You get up as fast as you can in the heavy suit of armor.  You ball up your armored fist."
				player_input(prompt="Do you swing your fist left or right?", choice1='Left', choice2='Right') #Prompt for user input	
				fistchoices=['right']
				response=raw_input('What is your choice?')
	
				while (response).lower() not in fistchoices:#User chooses Right or inputs incorrectly
					print" "
					print "Yikes!  Looks like you missed, try again."
				if (response).lower() in fistchoices[0]: #User chooses Left
					print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
					#import scribe_level3.py
#ARMORHESITATE
			if (response).lower() in cave0choices[1]: #User chooses to hesitate
				print "While you hesitate, the beast comes out of the cave and claws your armor.  You have a gash across your chest from the blow.  Your armor is in shards of metal beside you. You take a shard of metal and use it as a weapon."
				player_input(prompt='Do you use the shard of metal as a sword or a throwing weapon?',choice1='Sword', choice2='Throwing Weapon')
				shardchoices=['sword','throwing weapon']
				response=raw_input('What is your choice?')
	
				while (response).lower() not in shardchoices:
					print " "
					print "Incorrect input.  Try again."
					response=raw_input("What is your choice?").lower()
				if (response).lower() in shardchoices[0]: #User chooses to use as sword
					print "You use the metal shard as a sword.  As you swing left and right, the beast comes closer and closer.  You use the sword to deflect the fire the beast is blowing your way.  With your last ounce of strength, you thrust the metal shard into the beast.  You have killed the beast!"
					print " "
					print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
					#import scribe_level3.py
				if (response).lower() in shardchoices[1]:#User chooses to use as throwing weapon
					print "You use the metal shard as a throwing weapon. Since you have so many metal shards, you throw furiously at the beast.  The beast is dodging all of your shards!  As you come down to your last metal shard, you throw with all of your might.  The shard hits the beast's eye, and the trauma kills the beast!"
					print " "
					print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!!"  
					#import scribe_level3.py
			while (response).lower() not in cave0choices:
				print " "
				print "Incorrect input. Try again."
				response=raw_input("What is your choice?").lower()


#SWORD


		if (response).lower() in blacksmithchoices[1]: #User chooses hammer
			print 'The blacksmith smiles, creates a spiked hammer of magestic proportions, and gives it to you.  He calls you brave and bids you good luck.  You leave the blacksmith and travel to the cave where the beast is located.'
			player_input(prompt="Do you enter the cave or do you hesitate?",choice1="Enter", choice2="Hesitate") #Question/Prompt for user input
			cave1choices=['enter','hesitate'] #Dictionary for prompt choices			
			response=raw_input('What is your choice?') #raw input for response			
			if (response).lower() in cave1choices[0]: #User chooses to enter
				print "You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.   You quickly dodge out of the way.  In your action of dodging, you lost your spiked hammer in the dark!  You frantically search for it in the dark but you cannot find it. You decide to use your magical beer mug and you quickly pull it out.  It is too dark to see where the beast is."
				player_input(prompt='Do you wave your magical beer mug to the left or to the right?', choice1='Left', choice2='Right') #User prompted to wave quill left or right

				quillchoices=['right'] #Dictionary for prompt
				
				response=raw_input('What is your choice?') #raw input for response
				
				while (response).lower() not in quillchoices: #Input incorrect or user chose left
					print " "
					print "Yikes, looks like you missed.  Try again."
					response=raw_input("What is your choice?").lower()
				if (response).lower() in quillchoices[0]:#User chooses right
					print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!'
					#import scribe_level3.py
					
			if (response).lower() in cave1choices[1]: #User chooses to hesitate
				print "While you hesitate, the beast comes out of the cave and claws you across your chest.  You frantically grab your spiked hammer and swing it furiously at the beast, however, the beast is not fazed and becomes even stronger as it adapts to your blows.  You decide to use your hammer and the magic from your beer mug."
				player_input(prompt='Do you use your magical hammer as an offensive weapon or a defensive weapon?',choice1='Offensive weapon',choice2='Defensive weapon')
				
				magicalswordchoices=['offensive weapon', 'defensive weapon']

				response=raw_input("What is your choice?")

				while (response).lower() not in magicalswordchoices:
					print " "
					print "Incorrect input.  Try again."
					response=raw_input("What is your choice?").lower()
				if (response).lower() in magicalswordchoices[0]: #User chooses offensive weapon
					print "You use the magical hammer as a offensive weapon.  As you swing left and right, the beast comes closer and closer.  You use the hammer to hit the beast. You fight back and forth.  With your last blow to the beast, you swing with all your strength and kill the beast!"
					print " "
					print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
					#import scribe_level3.py
				if (response).lower() in magicalswordchoices[1]: #User chooses defensive weapon
					print "You use the magical hammer as a shield. You manage to deflect each fire blow from the beast.  As the beast runs out of breath from his firebreathing, you aim the shield directly at the beast.  As the beast breathes fire your way, the fire is deflected right back towards him and the beast is killed!"
					print " "
					print "Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!"  
					#import scribe_level3.py
					
			while (response).lower() not in cavechoices: #while loop for continuous program response if the user input is not found in the choices dictionary
				print " "
				print "Incorrect input. Try again."
				response=raw_input("What is your choice?").lower()	 
		while (response).lower() not in storychoices: #while loop for continuous program response if the user input is not found in the choices dictionary
			print " "
			print "Incorrect input. Try again."
			response=raw_input("What is your choice?").lower()

	while (response).lower() not in storychoices: #while loop for continuous program response if the user input is not found in the choices dictionary
		print " "
		print "Incorrect input. Try again."
		response=raw_input("What is your choice?").lower()
	if (response).lower() in storychoices[0]: #User chooses to ignore story
		print "You ignore his desperate look and change the topic with an embarassed look.  He gives you an understanding look and proceeds to give you blankets and bids you good night. The next morning, you wake before your savior does and you leave his village."
		#import scribe_level3.py
while (response).lower() not in painchoices: #while loop for continuous program response if the user input is not found in the choices dictionary
	print " "
	print "Incorrect input. Try again."
	response=raw_input("What is your choice?").lower()
if (response).lower() in painchoices[1]: #if the user input is equal to the second element in the array
	print "He says HMPH, brushes himself off, wipes away the tears from the pain, and walkas away angrily."
	print " "
	print "Because you chose to be a terrible person and let a handsome lad walk away angrily, 		you get caught by the palace guards and get returned to the palace!"
	#import scribe_level3.py
