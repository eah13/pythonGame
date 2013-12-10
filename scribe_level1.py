# -*- coding: utf-8 -*-
def player_input(prompt, choice1, choice2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice1;
	print "Choice 2: ", choice2;
	
print "Welcome to Chapter 1: Breakin' Bad Habits" #the title of the level prints 
print " "
print "As a result of your actions, you’re sent to the dungeon to think about what you've done." #this is an intro sentence for the Scribe's version of the game, level 1
print " "

player_input(prompt="What will you do in this dank and lonely cell? Break out or stay dank and lonely?", choice1="stay dank and lonely", choice2="break out") #Input asking the user if he/she wants to break out of the cell (and thus play the game) or not 
cellchoices=['stay dank and lonely', 'break out'] #choices dictionary for either styaing in cell or breaking out of it 
response= raw_input("What is your choice?") #raw input for response
if (response).lower() in cellchoices[0]:
  print "If you wish..." #Then this is the response that will print
 	import scribe_level1.py #And as a result, the user will be forced to the start of the scribe's version of level 1

if (response).lower() in cellchoise[1]:
  print "Excellent! You take out your handy dandy quill and begin lockpicking the door.\n" #Then the user has the ability   to lockpick the door 
  player_input(prompt="Do you turn your quill to the right or the left first?", choice1="left", choice2="right") #Input asking which way the user wants   to turn the quill to lockpick
  lockchoices= ['left', 'right']
  response= raw_input("What is your choice?") #raw input for response
  if (response).lower() in lockchoices[0]: #If the user turns it to the left
      print "The lock breaks free and your cell door swings open!" #Then the user is able to break free from the cell 
      player_input(prompt="Which door do you choose to leave from? Door one or door two?", choice1="one", choice2="two") #Input asking the user which door to   leave from
      response= raw_input("What is your choice?") #raw input for response 
      if (response).lower() in doorchoices[0]: #If the user chooses door one...
        print "Guards find you! You are manhandled and forced back into your cell.\n" #The user is forced back into his/her cell
        import scribe_level1.py #Then the user is forced to start the Scribe's version of level 1 over again
      if(reponse).lower() in doorchoices[1]: #If the user chooses door two...
        print "Fresh, clean air! You are free, Palace Scribe!"#The user is free
        import scribe_level2.py #And the user continues on to the Scribe's version of level 2

  if (response).lower() in lockchoices[1]: #If the user turns it to the right...
      print "The lock does not budge. Try again.\n" #Then the user is not able to open the door
      player_input(prompt="Do you turn your quill to the right or the left first?", choice1="left", choice2="right") #Input prompting the user to choose       which way to turn the quill to lockpick again
      newlockchoices=['left', 'right']
      reponse= raw_input("What is your choice?") #raw input for response
      if (response).lower() in newlockchoices[0]: #If the user turns it to the left
          print "The lock breaks free and your cell door swings open!" #Then the user is able to break free from the cell
      if (response).lower() in newlockchoices[1]: #If the user turns it to the right...
          print "The lock does not budge. Try again." #Then the user is not able to open the door
          import scribe_level1.py #The level restarts 
      
