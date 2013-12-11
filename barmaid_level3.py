def player_input(prompt, choice1, choice2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice1;
	print "Choice 2: ", choice2;

print "Welcome to Chapter 3: The Hung Jury!" 
print " "
print "You realize that you’re not cut out for a life on the run, so you decide to head back to the palace and stand trial. As the judge concludes your charges, you standand defiantly plead 'Not Guilty'\n"
print " "

player_input(prompt="What is your argument? Do you claim you were purposefully serving old beer because you heard that allowing it to ferment even longer was supposed to enhance the subtle flavors of a proper pale ale OR do you claim that while your beer-serving has been lax, your experiences in the forest have given you a mastery over brew, and you can use your knowledge to fortify your kingdom's brewing capabilities while harming enemies?)", choice1="proper Pale Ale", choice2="mastery over brew")#this is the first prompt to the user regarding healing

rebuttalchoices=['proper Pale Ale','mastery over brew'] #choices dictionary for the first prompt

response= raw_input("What is your argument?") #raw input for response

if (response).lower() in rebuttalchoices[0]: #User chooses to argue proper Pale Ale
	print "The king scoffs at your notion. 'A proper Pale Ale?? PAH! This be nothin' but a Pilsner-drinkin' kingdom lassie! I'm sentencing you to exile!"
	player_input(prompt="As the wagon carrying you and your fellow exiles travels down a path out of the kingdom, a swarm of marauding bandits charges past you in the direction of the kingdom. In the melee, you're set free from your chains and begin to escape! Suddenly though, you see the enemy's camp, and their supplies curiously unguarded. Do you poison their stores or scurry away into the forest?", choice1="poison their stores", choice2="scurry away to forest") #User prompted to ignore story or do something about the beast

	exilechoices=['poison their stores','scurry away to forest']

	response=raw_input("What is your choice?") #raw input for response

	if (response).lower() in exilechoices[0]: #User chooses to poison their stores
	  print " "
		print "You open up your flask and sprinkle a particularly nasty concoction into the various kegs scattered around the camp! Surely this will deal the enemy a crippling blow when they retreat for the night. Congratulations! You will assuredly be hailed a heroine upon your return to Karflooglesville...assuming you return. But will you? Stay tuned to the project to find out!" #and this is the result
		print " "

	while (response).lower() not in exilechoices: #while loop for continuous program response if the user input is not found in the choices dictionary
		print " "
		print "Incorrect input. Try again."
		response=raw_input("What is your choice?").lower()
	if (response).lower() in exilechoices[0]: #User chooses to scurry into the woods
		print "Well, you're hated in the kingdom, your love has abandoned you because your cowardice and you have nothing but ale. This isn't exactly going to plan. Maybe try again?"
		print "import barmaid_level3.py
		
while (response).lower() not in rebuttalchoices: #while loop for continuous program response if the user input is not found in the choices dictionary
	print " "
	print "Incorrect input. Try again."
	response=raw_input("What is your choice?").lower()
if (response).lower() in rebuttalchoices[1]: #User chooses to claim she has a mastery over brew
	print "The king considers your offer thoroughly. 'Hm' he ponders, 'So ye want to be our brewmaster...' Suddenly a loud crash is heard outside. 'MILORD' the king's page screams, 'We are besieged by the neighboring kingdom!' The king turns to you, 'Get down to to the keep with the other women and children! We'll discuss yer proposal later.' Down in the keep you spot a nearby keg. Surely you can make some concoction to boost the fighting soldiers' morale. With a keg in hand, you venture out to the courtyard in the midst of fighting forces. You spot both your lover and the king's son, both viciously wounded.\n"
	player_input(prompt="Who will you help? Your lover? Or the prince?", choice1="lover", choice2="prince"
	
	woundedchoices=['lover','prince']
	
	response=raw_input('What is your choice?')
	
	if (response).lower() in woundedchoices(0): #user has chosen their lover
	  print " "
	  print "You abandon the gasping prince and sprint to your lover. An enemy spots your sprint and readies his bow, firing an arrow that just misses you but plunges into the neck of your lover, ending his suffering. You step back in horror but come to your senses and rush back to the prince's aid, but it's too late, and the prince expires. The king is outraged that you would abandon his one heir. 'IT'S BACK TO THA DUNGEON FER YOU LASSIE!' he yells."
	  import barmaid_level1.py
	  
	while (response).lower() not in woundedchoices: #while loop for continuous program response if the user input is not found in the choices dictionary
	  print " "
    print "Incorrect input. Try again."
    response=raw_input("What is your choice?").lower()
	if (response).lower() in woundedchoices(1): #user has chosen the prince
	  print " "
	  print "You kneel down to the bleeding prince and quietly shove a healing salve into his mouth. The prince gulps all he can and starts to breathe a little more regularly. A nearby enemy archer scans over your location, but your lack of movement fools him and he continues his patrol. Quickly, your lift the prince into the safety of the keep and deftly roll a keg of ale to your lover's location, masking him from the enemy. Congratulations! You have saved the heir of Karflooglesville and surely are a heroine throughout all the land! But will the kingdom be able to fend off the enemy? Stay tuned to our project to find out!" #this is the end of the level
