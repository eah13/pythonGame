def player_input(prompt, choice_1, choice_2):
	"this prompts the player with the choices for the game"
	print "Prompt: ", prompt;
	print "Choice 1: ", choice_1;
	print "Choice 2: ", choice_2;

def program_answer_response(choice_dict_name, user_input_name):
	"prompts users incorrect answer when user inputs wrong thing"
	while (user_input_name).lower() not in choice_dict_name:
		print " "
		print "Incorrect input.  Try again."
		user_input_name=raw_input("What is your choice?")
	if (user_input_name).lower() in choice_dict_name:
		print "awesome"
