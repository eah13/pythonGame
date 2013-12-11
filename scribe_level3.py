def player_input(prompt, choice1, choice2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice1;
	print "Choice 2: ", choice2;

print "Welcome to Chapter 3: The Hung Jury!" 
print " "
print "You realize that you’re not cut out for a life on the run, so you decide to head back to the palace and stand trial. As the judge concludes your charges, you standand defiantly plead 'Not Guilty'\n"
print " "

player_input(prompt="What is your argument? Do you claim you were taking notes in such a way to establish a new metadata schemeand usher in the educational practice of information science OR do you claim your experiences in the forest will make you a valuable warrior for the kingdom?)", choice1="Information science", choice2="valuable warrior")#this is the first prompt to the user regarding their argument to the king

rebuttalchoices=['Information science','valuable warrior'] #choices dictionary for the first prompt

response= raw_input("What is your argument?") #raw input for response

if (response).lower() in rebuttalchoices[0]: #User chooses to argue Information science
	print "The king scoffs at your notion. '98% of our kingdom cannot even read. INFORMATION SCIENCE PAH?! I condemn you to the guillotine! Ouch, sounds like the king isn't the only one losing his head over this." 
	player_input(prompt="As you approach the guillotine, the neighboring kingdom suddenly attacks the courtyard. You still have your quill in the seat of your pants. Do you stay and defend the kingdom or take the opportunity to run?", choice1="stay and defend the kingdom", choice2="take the opportunity to run") #User prompted to ignore story or do something about the beast

	guillotinechoices=['stay and defend the kingdom','take the opportunity to run']

	response=raw_input("What is your choice?") #raw input for response

	if (response).lower() in guillotinechoices[0]: #User chooses to defend the kingdom
	  print " "
		print ""You withdraw your quill and line up next to the king's guard. 'FOR HONOR' you yell. Congratulations! Your heroic deeds have successfully cleared your name throughout all of Karflooglesville. But will you be able to fend off the guards? Stay tuned to the project to find out!" #and this is the result
		print " "

	while (response).lower() not in guillotinechoices: #while loop for continuous program response if the user input is not found in the choices dictionary
		print " "
		print "Incorrect input. Try again."
		response=raw_input("What is your choice?").lower()
	if (response).lower() in guillotinechoices[1]: #User chooses to run away
		print "The king catches you running away in the melee and orders a knight after you. You're no match for the horse's speed, and the king orders an execution on the spot. Game over. Just kidding, care to try again?"
		print "scribe_level3.py
		
while (response).lower() not in rebuttalchoices: #while loop for continuous program response if the user input is not found in the choices dictionary
	print " "
	print "Incorrect input. Try again."
	response=raw_input("What is your choice?").lower()
if (response).lower() in rebuttalchoices[1]: #User chooses to claim he is a valuable warrior
	print "The king considers your offer thoroughly. 'Hm' he ponders, 'We have been short a few heroes recently.' Suddenly a loud crash is heard outside. 'MILORD' the king's page screams, 'We are besieged by the neighboring kingdom!' The king turns to you, 'Alrighty lad, you say you'll be a valuable warrior, now's the time to prove it."
	player_input(prompt="Do you rush to meet the enemy head on? Or do you stay back, slowly ponder your surroudings and quickly make a break for the back gate?", choice1="head on", choice2="back gate"
	
	courtyardchoices=['head on','back gate']
	
	response=raw_input('What is your choice?')
	
	if (response).lower() in courtyardchoices(0): #user has chosen to rush the enemy head on
	  print " "
	  print "You cautiously but confidently approach the enemy in the company of the king's guard. Quickly, you draw your quill (no pun intended), causing the enemy to burst into laughter. Congratulations! Your heroic deeds have successfully cleared your name throughout all of Karflooglesville. But will you be able to fend off the guards? Stay tuned to the project to find out!"
	  
	while (response).lower() not in courtyardchoices: #while loop for continuous program response if the user input is not found in the choices dictionary
	  print " "
    print "Incorrect input. Try again."
    response=raw_input("What is your choice?").lower()
	if (response).lower() in courtyardchoices(1): #user has chosen to make a break for the back gate
	  print " "
	  print "The back gate is right behind the dungeon. Unfortunately, the dungeon master is privy to your plan and halts you. Your quill barely scratches his imposing armor and thick mask 'Back in the cell ya go, laddie,' he says, tossing you in the familiarity of your cell. Dammit, not again\n" #this is the end of our first go at the project, but if you're creating a new level obviously end it however you want
    import scribe_level1.py #...it sends you back to the dungeon, so you restart the whole game.
