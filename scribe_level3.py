# -*- coding: utf-8 -*-

import functions.py #this imports several crucial functions
print "Welcome to Chapter 3: Hung Jury" #this is the title of the chapter
print " "
print "You realize that you’re not cut out for a life on the run, so you decide to head back to the palace and stand trial. As the judge concludes your charges, you standand defiantly plead 'Not Guilty'\n"
print " "
player_input(prompt="What is your argument? Do you claim you were taking notes in such a way to establish a new metadata schemeand usher in the educational practice of information science OR do you claim your experiences in the forest will make you a valuable warrior for the kingdom?)
king_rebuttal - raw_input("What is your argument? Do you claim you were taking notes in such a way to establish a new metadata schemeand usher in the educational practice of " + "\"information science\"" + ' OR do you claim your experiences in the forest will make you a " + "\"valuable warrior\"" + ' for the kingdom?) #this gives the players their two options to pick
if 'Information science' in king_rebuttal: #this is one of the possible answers, it needs to be case sensitive so keep it in mind
  print " "
  print "The king scoffs at your notion. '98% of our kingdom cannot even read. INFORMATION SCIENCE PAH?! I condemn you to the guillotine! Ouch, sounds like the king isn't the only one losing his head over this." #this input continues the story depending on what the player chose
  print " "
  guillotine = raw_input("As you approach the guillotine, the neighboring kingdom suddenly attacks the courtyard. You still have your quill in the seat of your pants. Do you " + "\"stay and defend the kingdom\"" + ' or '+ "\"take the opportunity to run\""+'?'))
  if 'stay and defend the kingdom' in guillotine: #this is a specific choice a player can make once they've chosen this branch
      print " "
      print "You withdraw your quill and line up next to the king's guard. 'FOR HONOR' you yell. Congratulations! Your heroic deeds have successfully cleared your name throughout all of Karflooglesville. But will you be able to fend off the guards? Stay tuned to the project to find out!"
      print " "
  if 'take the opportunity to run' in guillotine: #this is the alternate choice
      print " "
      print "The king catches you running away in the melee and orders a knight after you. You're no match for the horse's speed, and the king orders an execution on the spot. Game over. Just kidding, care to try again?"
      print "import scribe_level3.py" #it was the 'wrong' choice so it forces the player to restart the level
  

if 'Valuable warrior' in action: #this lays out the story for players that chose the second option
  print "The king considers your offer thoroughly. 'Hm' he ponders, 'We have been short a few heroes recently.' Suddenly a loud crash is heard outside. 'MILORD' the king's page screams, 'We are besieged by the neighboring kingdom!' The king turns to you, 'Alrighty lad, you say you'll be a valuable warrior, now's the time to prove it.'\n"
  courtyard = raw_input("Do you " + "\"Meet the enemy head on\"" + ' or do you stay back, nervously observing your surroundings and making a break for the " + "\"back gate\"" + ' while the king is distracted?") 
  if 'Meet the enemy head on' in courtyard: #here's the first choice
      print " "
      print "You cautiously but confidently approach the enemy in the company of the king's guard. Quickly, you drawyour quill (no pun intended), causing the enemy to burst into laughter. Congratulations! Your heroic deeds have successfully cleared your name throughout all of Karflooglesville. But will you be able to fend off the guards? Stay tuned to the project to find out!"\n"
  if 'back gate' in courtyard:
      print " "
      print "The back gate is right behind the dungeon. Unfortunately, the dungeon master is privy to your plan and halts you. Your quill barely scratches his imposing armor and thick mask 'Back in the cell ya go, laddie,' he says, tossing you in the familiarity of your cell. Dammit, not again\n" #this is the end of our first go at the project, but if you're creating a new level obviously end it however you want
      print "import scribe_level1.py" #...it sends you back to the dungeon, so you restart the whole game.
