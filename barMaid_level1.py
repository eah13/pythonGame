character2 = {'Name': 'Bar Maid', 'Gender': 'Female', 'Role': 'Serving alcoholic beverages to the king'};

barMaid_level1 = ['dungeon', 'cell', 'window'];

print "Chapter 1: Breakin' Bad Habits"

print "As a result of your actions, you’re sent to the dungeon to think about what you've done.\n"

action = raw_input("What will you do in this dank and lonely cell? Break out or stay dank and lonely?\n")
if 'Stay dank and lonely' in action:
  print "If you wish..."
  import scribe_level1.py

if 'Break out' in action:
  print "Excellent!"
  escape = raw_input("...But how will you break out? The way I see it, you have two options. Break down the cell door with   your highly reliable beer mug or break the conveniently located window right behind you?\n")
  if 'Break down cell door' in escape:
  print "Alas, to no avail."
  
  if 'Break window' in escape:
  print "Somehow you've managed to break the window quietly enough not to attract any attention from the dungeon guards or your fellow dungeon mates. You escape successfully!" 
  
  location = raw_input("Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the      nearing forest, or back to the palace?"
  if 'Forest' in location: 
  import barMaid_level2.py
  
  if 'Palace' in location:
  print "What are you doing?! You can't go back there, the King'll have your head for sure!"
  
  decision = raw_input("Do you really want to go back?")
  if 'Yes' in decision:
  print "The King spots you sneaking across the grounds while he is on one of his evening strolls. He is merciful and     sends you back to the dungeon."
  
  if 'No' in decision:
  print "Good. I knew you were wiser than that."
  location = raw_input("Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the      nearing forest, or back to the palace?"
  if 'Forest' in location: 
  import barMaid_level2.py
  
  
  