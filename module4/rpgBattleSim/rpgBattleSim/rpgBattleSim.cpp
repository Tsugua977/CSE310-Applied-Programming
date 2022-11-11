// rpgBattleSim.cpp : This file contains the 'main' function. Program execution begins and ends there.

#include <iostream>
#include <string>

int main(){
    //Sets up player's health, the enemy's health, and amount of thunder spells.
    int playerHP = 15;
    int goblinHP = 12;
    int thunderAmount = 2;

    //Sets the win condition to false.
    bool winCondition = false;

    //Asks the user if they want to play.
    int userResponse;
    std::cout << "Welcome to RPG Battle Simulator! Would you like the fight? \n (Press 1 for yes, and 2 for no.) ";
    std::cin >> userResponse;
    
    //If the user press 1, the game commences.
    if (userResponse == 1) {
        std::cout << "Battle commence!\n";
    }
    //If the player presses 2, the program stops.
    else {
        return 0;
    }

    //Prints intro text.
    std::cout << "While under the cover of the forest, a war cry is heard! A goblin jumps out in front of you, branishing a rusty dagger with a wicked sneer across his face. \n";

    //While the win condition is false, the game runs.
    while (winCondition == false) {
        //Sets up the inventory ui.
        std::cout << "1) Attack\n";
        std::cout << "2) Inventory\n";
        std::cout << "3) Run Away\n";
        //Prints the user's health.
        std::cout << "Your HP:" << playerHP << "\n";
        //Asks what the player what they want to do.
        std::cout << "What do you want to do? ";
        std::cin >> userResponse;
        std::cout << "\n";

        //Runs if the user presses 1 to attack.
        if (userResponse == 1) {
            //Supposed to randomly generate a value for the player's attack damage.
            int playerDamage = rand() % 6 + 1;
            //Subtracts the enemy's health from the player's attack. 
            goblinHP -= playerDamage;
            //Prints out how much damage the player deals.
            std::cout << "You dealt " << playerDamage << " damage to the goblin! \n";

            //Checks if the goblin's health is 0. If it is, the game ends.
            if (goblinHP <= 0) {
                std::cout << "The goblin slumps to the forest floor, lifeless. You have won the battle! \n";
                return 0;
            }
            //If the goblin's health is not 0, the goblin attacks.
            else {
                //Supposed to randomly generate a value for the goblin's attack damage.
                int goblinDamage = rand() % 6 + 1;
                //Subtracts the player's health from the goblin's attack. 
                playerHP -= goblinDamage;
                //Prints out how much damage the goblin deals.
                std::cout << "The goblin strikes and deals " << goblinDamage << " damage to you! \n";
            }
        }
        //Runs if the user presses 2 to open the inventory.
        else if (userResponse == 2) {
            //Sets up the player's inventory reponse.
            int inventoryResponse = 0;
            //While the inventoryReponse is 0, the inventory loop runs.
            while (inventoryResponse == 0) {
                //Updates the amount of thunder spells.
                thunderAmount = thunderAmount;
                //Sets up the inventory ui.
                std::cout << "1) Health Potion\n";
                std::cout << "2) Thunderspell (" << thunderAmount << ") \n";
                //Asks the player what they want to do in the inventory.
                std::cout << "Select what you want to do. ";
                std::cin >> userResponse;
                std::cout << "\n";
                //Runs if the user selects 1 to drink a health potion.
                if (userResponse == 1) {
                    //Adds 4 health to the player's health.
                    playerHP += 4;
                    //Prints out the health statement.
                    std::cout << "You drink the health potion. You gain 4 HP back!\n";
                    //Sets inventoryResponse to 1, breaking out of the loop.
                    inventoryResponse = 1;
                }
                //Runs if the user selects 2 to use a thunder spell.
                else if (userResponse == 2) {
                    //If there are no more thunder spells, this statement is printed and the inventory loop isn't broken.
                    if (thunderAmount == 0) {
                        std::cout << "You have no more of these!\n";
                    }
                    else {
                        //If there are more than 0 thunder spells, then this is run.
                        //Supposed to randomly generate a value for the thunder's damage.
                        int thunderDamage = rand() % 8 + 3;
                        //Subtracts the enemy's health from the player's attack. 
                        goblinHP -= thunderDamage;
                        //Prints out how much damage the spell deals.
                        std::cout << "You cast the spell and the goblin takes " << thunderDamage << " damage.\n";
                        thunderAmount -= 1;
                        //Supposed to randomly generate a value for the goblin's attack damage.
                        int goblinDamage = rand() % 6 + 1;
                        //Subtracts the player's health from the goblin's attack. 
                        playerHP -= goblinDamage;
                        //Prints out how much damage the goblin deals.
                        std::cout << "The goblin strikes and deals " << goblinDamage << " damage to you! \n";
                        //Sets inventoryResponse to 2, breaking out of the loop.
                        inventoryResponse = 2;
                    }
                }
                //If the player does not input a correct option, this statement runs and the inventory loop continues.
                else {
                    std::cout << "That's not an option!\n";
                }
            }
        }
        //Runs if the user presses 3 to run away.
        else if (userResponse == 3) {
            //This statement prints when this if loop is run.
            std::cout << "\n";
            std::cout << "You turn away and run for dear life, as you hear the goblin cackle behind you. You escape with your life. \n";
            //The game ends.
            return 0;
        }
        //If the player does not input a correct option, this statement runs and the game while loop continues.
        else {
            std::cout << "That's not an option! Turn and fight!\n";
        }

        //If the player's health is 0, the game ends.
        if (playerHP <= 0) {
            std::cout << "You stumble to the ground as you realize the goblin has stabbed you in the chest. You're vision goes black.\n You died! \n";
            return 0;
        }
        //If the player's health is not 0, the game continues.
        else {
            std::cout << "\n";
        }
    }
}