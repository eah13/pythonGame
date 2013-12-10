# -*- coding: utf-8 -*-

import functions.py #this imports several crucial functions
print "Welcome to Chapter 3: Hung Jury"  #this is the title of the chapter
print " "
print "You realize that you’re not cut out for a life on the run, so you decide to head back to the palace and stand trial. As the judge concludes your charges, you standand defiantly plead 'Not Guilty'\n"
print " "
player_input(prompt="What is your argument? Do you claim you were purposefully serving old beer because you heard that allowing it to ferment even longer was supposed to enhance the subtle flavors of a proper pale ale OR do you claim that while your beer-serving has been lax, your experiences in the forest have given you a mastery over brew, and you can use your knowledge to fortify your kingdom's brewing capabilities while harming enemies?)
king_rebuttal - raw_input("What is your argument? Do you claim you were purposefully serving old beer because you heard that allowing it to ferment even longer was supposed to enhance the subtle flavors of a " + "\"proper Pale Ale\"" + ' OR do you claim that while your beer-serving has been lax, your experiences in the forest have given you a " + "\"mastery over brew\"" + ', and you can use your knowledge to fortify your kingdom's brewing capabilities while harming enemies?) #this gives the players their choices to pick to advance the story
if 'proper Pale Ale' in king_rebuttal: #this is one of the possible answers, it needs to be case sensitive so keep it in mind
  print " "
  print "The king scoffs at your notion. 'A proper Pale Ale?? PAH! This be nothin' but a Pilsner-drinkin' kingdom lassie! I'm sentencing you to exile!'."
  print " "
  exile = raw_input("As the wagon carrying you and your fellow exiles travels down a path out of the kingdom, a swarm of marauding bandits charges past you in the direction of the kingdom. In the melee, you're set free from your chains and begin to escape! Suddenly though, you see the enemy's camp, and their supplies curiously unguarded. Do you " + "\"poison their stores\"" + ' or '+ "\"scurry away into the forest\""+'?') #this input continues the story depending on what the player chose
  if 'poison their stores' in exile: #this is a specific choice a player can make once they've chosen this branch
      print " "
      print "You open up your flask and sprinkle a particularly nasty concoction into the various kegs scattered around the camp! Surely this will deal the enemy a crippling blow when they retreat for the night. Congratulations! You will assuredly be hailed a heroine upon your return to Karflooglesville...assuming you return. But will you? Stay tuned to the project to find out!" #and this is the result
      print " "
  if 'scurry away to the forest' in exile: #this is the alternate choice
      print " "
      print "Well, your hated in the kingdom, your love has abandoned you because your cowardice and you have nothing but ale. This isn't exactly going to plan. Maybe try again?"
      print "import barmaid_level3.py" #it was the 'wrong' choice so it forces the player to restart the level
  

if 'mastery over brew' in king_rebuttal: #this lays out the story for players that chose the second option
  print "The king considers your offer thoroughly. 'Hm' he ponders, 'So ye want to be our brewmaster...' Suddenly a loud crash is heard outside. 'MILORD' the king's page screams, 'We are besieged by the neighboring kingdom!' The king turns to you, 'Get down to to the keep with the other women and children! We'll discuss yer proposal later.' Down in the keep you spot a nearby keg. Surely you can make some concoction to boost the fighting soldiers' morale. With a keg in hand, you venture out to the courtyard in the midst of fighting forces. You spot both your lover and the king's son, both viciously wounded.\n"
  important_choice = raw_input("Do you " + "\"tend to the aid of your lover\"" + ' or " + "\"tend to the aid of the prince\"" + ' while the king is distracted?") #this expands the story and tells the players what choices they can make
  if 'tend to the aid of your lover' in important_choice: #here's the first choice
      print " "
      print "You abandon the gasping prince and sprint to your lover. An enemy spots your sprint and readies his bow, firing an arrow that just misses you but plunges into the neck of your lover, ending his suffering. You step back in horror but come to your senses and rush back to the prince's aid, but it's too late, and the prince expires. The king is outraged that you would abandon his one heir. 'IT'S BACK TO THA DUNGEON FER YOU LASSIE!' he yells."\n"
      print "import barmaid_level1.py" #...it sends you back to the dungeon, so you restart the whole game.
  if 'tend to the aid of the prince' in important_choice: #this is the second choice
      print " "
      print "You kneel down to the bleeding prince and quietly shove a healing salve into his mouth. The prince gulps all he can and starts to breathe a little more regularly. A nearby enemy archer scans over your location, but your lack of movement fools him and he continues his patrol. Quickly, your lift the prince into the safety of the keep and deftly roll a keg of ale to your lover's location, masking him from the enemy. Congratulations! You have saved the heir of Karflooglesville and surely are a heroine throughout all the land! But will the kingdom be able to fend off the enemy? Stay tuned to our project to find out!\n" #this is the end of our first go at the project, but if you're creating a new level obviously end it however you want.
      
