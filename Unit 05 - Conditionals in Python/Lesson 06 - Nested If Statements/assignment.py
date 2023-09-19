#Make an little piece of an text based adventure game
#You don't have to copy what I've done but use it as a template to get your mind going.  

player_choice = input("Pick a direction to walk (Up, Down, Left, Right)")
if player_choice == "Up":
    print("You have encountered a dragon")
    player_choice_2 = input("What do you do (Fight, Retreat)")
    if player_choice_2 == "Fight":
        print("You got eaten by the dragon (Game Over")
    else:
        print("You live to play another day")
elif player_choice == "Right":
    #come up with some other story followed with if statement. 