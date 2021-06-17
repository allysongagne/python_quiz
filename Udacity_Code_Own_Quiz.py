#Udacity Introduction to Programming Nanodegree, Code Your Own Quiz Project.
#Game topic: Boston Red Sox baseball team
#Game has three levels: Rookie (easy), All-Star (medium), and MVP (hard).

#Quiz Questions.
questions_rookie = """\nThe Boston Red Sox play at ___1___ park, located in Boston, MA. 
The Red Sox won their first World Series title in ___2___ against the Pittsburgh ___3___. 
The name of the mascot is ___4___."""
questions_allstar = """\nThe Boston Red Sox have an infamous rivalry with the ___1___. This 
rivalry became more intense after the sale of ___2___ which was dubbed the curse of the ___3___. 
It took the Red Sox ___4___ years to win another World Series title and to break the curse."""
questions_mvp = """\nThe 1967 Boston Red Sox season was nicknamed the ___1___ and they faced 
the ___2___ in the World Series. The Red Sox have ___3___ minor league affiliate teams. The 
hit song by Neil Diamond ___4___ is often played at games."""

#Quiz Answers. 
answers_rookie = ["fenway", "1903", "pirates", "wally"]
answers_allstar = ["new york yankees", "babe ruth", "bambino", "86"]
answers_mvp = ["impossible dream", "st. louis cardinals", "8", "sweet caroline" ]

#Blanks that will be replaced.
blanks = ["___1___", "___2___", "___3___", "___4___"]

#Player introduction to game. 
def welcome():
        """
        Welcomes and prompts player to provide their name and inquires if player wants to play game.
        Inputs: Prompt inquiring player's name and if the player is ready to play.
        Outputs: Greeting and name player provided.  
        """
        print ("Welcome to the Ultimate Boston Red Sox Trivia Game\n")
        name = raw_input ("What is your name? ")
        print ("Hi " +name+ "!")
        start = raw_input ("Ready to Test your Baseball Knowledge?? ").lower()
        if start == ("yes"):
                print ("\nBatter Up!") 
        else: 
                print ("See you next time! Bye!")
                return welcome()

#Game level selection. 
def level_selection():
        """
        Prompts player to select game difficulty level. If player's selection does not match avaiable options,
        player will be prompted to select again.   
        Input: Game level options: Rookie, All-Star or MVP
        Output: Questions and answers corresponding to level selected by player. Level player selected.    
        """
        game_level = raw_input ("\nSelect Game Level: Rookie (easy), All-Star (medium) or MVP (hard): ").lower()
        if game_level == ("rookie"):
                print ("You Selected: Rookie")
                return questions_rookie, answers_rookie
        elif game_level == ("all-star"):
                print ("You Selected: All-Star")
                return questions_allstar, answers_allstar
        elif game_level == ("mvp"):
                print ("You Selected: MVP")
                return questions_mvp, answers_mvp
        else: 
                print ("Error: Wrong Selection")
                return level_selection()

#Runs Game.
def main():
        """
        Prompts player's introduction to game, questions and answers for level selected. Checks player_answer and if correct
        replaces player_answer within question paragraph. When game is completed player wins and is asked to play
        again. If player selects to play again then game restarts.
        """
        welcome()
        index = 0
        level, answer = level_selection()
        while index < len (blanks):
                print level
                player_answer = raw_input ("\nEnter missing word for "+ blanks[index]+":").lower()
                if player_answer == answer[index]:
                        print ("\nHome Run!")
                        level = level.replace(blanks[index], player_answer)
                        index += 1
                else:
                        print ("\nStrike!")
        print ("Congrats! You're a Series Champ!")
        next_game = raw_input ("Play Again? ").lower()
        if next_game == ("yes"):
                return main()
        else:
                print ("See You Next Time! Bye!")
main()

