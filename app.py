#1. Proper use of Dunder Main
if __name__ == '__main__':
        
    #2. Import player data and tools
    from constants import TEAMS, PLAYERS
    from itertools import chain
    
    #3. Create a clean_data function
    def clean_data(data):
        cleaned = []
        for player in data:
            fixed = {}
            fixed["name"] = player["name"]
            fixed["height"], test = player["height"].split(" ")
            fixed["height"] = int(fixed["height"])
            fixed["experience"] = player["experience"]
            if fixed["experience"].lower() == 'yes':
                fixed["experience"] = True
            else:
                fixed["experience"] = False
            fixed["guardians"] = player["guardians"].split(" and ")
            cleaned.append(fixed)
        return cleaned     
    
    #4. Create a balance_teams function
    #Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.
    #HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)
    
    def balance_teams(players):
        num_players = int(len(players) / len(TEAMS))
        experience = []
        no_experience = []
        global panthers, bandits, warriors
        panthers = []
        bandits = []
        warriors = []
        
        #Additionally, balance the teams so that each team has the same number of experienced vs. inexperienced players.
        for player in players:
            if player["experience"] == True:
                experience.append(player)
            else:
                no_experience.append(player)
                
        for num, player in enumerate(experience):
            if num % 3 == 0:
                panthers.append(player)
            elif num % 2 == 0:
                bandits.append(player)
            else:
                warriors.append(player)

        for num, player in enumerate(no_experience):
            if num % 3 == 0:
                panthers.append(player)
            elif num % 2 == 0:
                bandits.append(player)
            else:
                warriors.append(player)
        return panthers, bandits, warriors
    
    #5. Console readability matters
    #6. Displaying the stats
    def display_stats(players, name):
        #save number of inexperienced/experienced players on that team
        experience = 0
        no_experience = 0
        #Organize Players by Height (got code from: shorturl.at/lOT04)
        players = sorted(players, key=lambda x: x['height'])
        height = 0
        names = []
        guardians = []
        
        for player in players:
            if player["experience"] is True:
                experience += 1
            else:
                no_experience += 1
            height += player["height"]
            names.append(player["name"])
            guardians.append(player["guardians"])
        
        #save the average height of the team
        av_height = round(height / len(players))
        
        names = ", ".join(names)
        guardians = list(chain.from_iterable(guardians))
        guardians = ", ".join(guardians)
        
        print(f"\nTeam name is {name}.\n"
            f"There are {len(players)} total members of the team.\n"
            f"Number with experience: {experience}. Number with no experience: {no_experience}.\n"
            f"The average height of the team is {av_height} inches.\n\n"
            f"Players' Names (from shortest to tallest): {names}.\n\n"
            f"Guardians: {guardians}.\n") 
        #see menu again
        while True:
            see_again = input("Would you like to see another team's stats? Yes or No:\n")
            if see_again.lower() == 'yes':
                run_menu(TEAMS, PLAYERS)
            elif see_again.lower() == 'no':
                print("Have a good day, goodbye!")
                exit()
            else:
                print("Invalid Response. Please type 'yes' or 'no'.")
                continue
    
    #make the menu
    #Quit Menu option included
    def run_menu(teams, players):
        cleaned = clean_data(players)
        balance_teams(cleaned)
        print("""
WELCOME TO THE BASKETBALL TEAM STATS TOOL

---- MENU----

Here are your choices:
  A) Display Panthers' Stats
  B) Display Bandits' Stats
  C) Display Warriors' Stats
  D) Quit
        """)
        try:
            while True:
                user_input = input("Please enter an option:\n")
                
                if user_input.lower() == 'a':
                    display_stats(panthers, "Panthers")
                elif user_input.lower() == 'b':
                    display_stats(bandits, "Bandits")
                elif user_input.lower() == 'c':
                    display_stats(warriors, "Warriors")
                elif user_input.lower() == 'd':
                    print("Have a good day, goodbye!")
                    exit()
                else:
                    print("Invalid Response. Please type 'a', 'b', 'c', or 'd'.")
                    continue
        except ValueError:
            print("Invalid response, please try again.")
            run_menu(TEAMS, PLAYERS)
    
    run_menu(TEAMS, PLAYERS)
