# Program that will search players OPGG by name entered and will put the winrate, League Points, and rank
# Done through Selenium API

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def main():
    # Gets name of player we are going to look up on OPGG
    name = input("Enter in the User Name of the User you'd like to search\n")

    # Starts the selenium driver and directs it to the OPGG website
    source_driver = 'chromedriver.exe'
    driver = webdriver.Chrome(source_driver)
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

        # Prints out the data to the screen
        print(rank.text + " " + lp_amount.text + '\n')
        print(win_ratio.text + "\n")

        # Quits out of the driver
        driver.quit()

    except:
        # Sets the rank as Unranked, prints it out, and then quits the driver
        rank = "Unranked"

        print(rank + '\n')

        driver.quit()


main()
