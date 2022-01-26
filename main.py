# Program that will search players OPGG by name entered and will put the winrate, League Points, and rank
# Done through Selenium API

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from player import Player


def print_ui():
    print("1. Add a Player")
    print("2. Look up Player")
    print("3. See Player List")
    print("0. Quit Program")
    return


def get_player_data(name):
    # Starting the Selenium driver
    source_driver = 'chromedriver.exe'
    driver = webdriver.Chrome(source_driver)

    # Going to OPGG
    driver.get("https://na.op.gg/")

    # Enter the name into the search bar
    search_bar = driver.find_element(By.ID, 'searchUserName')
    search_bar.send_keys(name)
    search_bar.send_keys(Keys.ENTER)

    try:
        # Changes player's page over to the rank tab
        ranked_tab = driver.find_element(By.ID, "right_gametype_soloranked")
        ranked_tab.click()

        # Waits until the player's rank can be located, if not we know its an unranked player
        rank = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, "TierRank"))
        )

        # Gets the League Points and win_ratio
        lp_amount = driver.find_element(By.CLASS_NAME, "LeaguePoints")
        win_ratio = driver.find_element(By.CLASS_NAME, "winratio")

        return Player(name, rank.text, lp_amount.text, win_ratio.text)
        # Quits out of driver

        #


    except:
        # Sets the rank as Unranked, prints it out, and then quits the driver
        driver.quit()

        return Player(name, "Unranked", "None", "None")


def main():
    # Initializes the variable that holds the selection of the user
    option: str = "none"

    Players = []
    # Starting the selenium driver
    # Make it where selenium starts up on its self everytime we just do option 1 and exits after
    while option > '0':
        # Prints out the ui and asks the user for input
        print_ui()
        option = input()
        # Adds a player to the list
        if option == '1':
            name = input("What is the Player's username?\n")
            Players.append(get_player_data(name))

            print("Player successfully added")

            pass

        # Looks up a player's name in the list
        if option == '2':
            name = input("What is the Player's username?\n")
            name_check: int = 0
            for player in Players:
                if name == player.get_user_name():
                    print(player.get_user_name() + "\n" +
                          player.get_rank() + " " +
                          player.get_lp() + " LP " +
                          player.get_win_ratio() + "\n")
                    name_check = 1
            if name_check == 0:
                print("Player Not Found \n")
            pass

        # Prints out the entire List
        if option == '3':
            count = 1
            for player in Players:
                print(str(count) + '. '
                      + player.get_user_name() + ' | '
                      + player.get_rank() + " | "
                      + player.get_lp() + "LP  | "
                      + player.get_win_ratio() + " | ")
                count = count + 1
            pass


main()
