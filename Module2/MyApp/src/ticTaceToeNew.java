import java.util.*;
import java.util.random.*;

public class ticTaceToeNew {
    
    //Main function.
    public static void main(String[] args) throws Exception {
        
        //Creates and populates the board array.
        String[] boardArray = {"1","2","3","4","5","6","7","8","9"};
        //Creates the winner condition.
        boolean winner = false;
        //Prints the board.
        printBoard(boardArray);
        //Creates a while loop to replay the gameplay.
        while (winner == false){
            //Asks the user for a number to place on the board.
            Scanner player1 = new Scanner(System.in);
            System.out.println("Pick a number from 1-9 to place your X:");
            int boardSpot = player1.nextInt();
            //Checks if the player's number is on the board.
            boolean result = isValid(boardSpot, boardArray);
            //If the player's number isn't on the board, the program will ask the player
            //for a new number.
            while (!result) {
                System.out.println("That spot is not open. Please choose a different spot.");
                boardSpot = player1.nextInt();
                result = isValid(boardSpot, boardArray);
            }
            //Subtracts 1 from the player's input to accuratly put their symbol on the board.
            boardSpot -= 1;
            //Places the user's postion on the board.
            placementXO(boardArray, boardSpot, "user");
            //Checks if the user or computer wins.
            winner = isGameOver(boardArray);
            //If either the user or computer wins, it breaks out of the loop.
            if (winner == true){
                break;
            } else {
                System.out.println("");
            }
            //Prints the board.
            printBoard(boardArray);
            //Makes a line space between the boards.
            System.out.println("\n");
            //Creates a random value.
            Random randNum = new Random();
            //A random number is chosen between the range of 1-9.
            int computerPos = randNum.nextInt(9);
            //Checks if the computer's value is in the array.
            result = isValid(computerPos, boardArray);
            //If the player's number isn't on the board, the program will ask the player
            //for a new number.
            while (!result) {
                computerPos = randNum.nextInt(9);
                result = isValid(computerPos, boardArray);
            }
            //Subtracts one from the computer's value.
            computerPos -= 1;
            //Places the user's postion on the board.
            placementXO(boardArray, computerPos, "computer");
            //Prints the board.
            printBoard(boardArray);
            //Checks if the user or computer wins.
            winner = isGameOver(boardArray);
            //If either the user or computer wins, it breaks out of the loop.
            if (winner == true){
                break;
            } else {
                System.out.println("\n");
            }
        }
    }
    //Class that prints out the board on the screen.
    static void printBoard(String[] boardArray) 
    {
        System.out.println("| " + boardArray[0] + " | " + boardArray[1] + " | " + boardArray[2] + " |");
        System.out.println("| - | - | - |");
        System.out.println("| " + boardArray[3] + " | " + boardArray[4] + " | " + boardArray[5] + " |");
        System.out.println("| - | - | - |");
        System.out.println("| " + boardArray[6] + " | " + boardArray[7] + " | " + boardArray[8] + " |");
    }
    //Class that checks if the user's or computer's chosen position is in the array.
    public static boolean isValid(int boardSpot, String[] boardArray){
        //Changes the array into a list.
        List<String> list = Arrays.asList(boardArray);
        //Changes the chosen spot from an int to a string.
        String spotStr = String.valueOf(boardSpot);
        //If the value is in the list, it returns true. Else, it returns false.
        if (list.contains(spotStr)){
            return true;
        } else {
            return false;
        }
    }
    //Places the X or O based on if the user or the computer was put in this function.
    public static void placementXO(String[] boardArray, int pos, String player){
        //Creates a symbol string.
        String symbol = "X";
        //If the user was put into the class, the symbol is changed to X.
        if (player == "user"){
            symbol = "X";
        //If the computer was put into the class, the symbol is changed to O.
        } else if (player == "computer"){
            symbol = "O";
        }
        //Checks the input value and places the symbol there.
        switch (pos) {
            case 0:
                boardArray[0] = symbol;
                break;
            case 1:
                boardArray[1] = symbol;
                break;
            case 2:
                boardArray[2] = symbol;
                break;
            case 3:
                boardArray[3] = symbol;
                break;
            case 4:
                boardArray[4] = symbol;
                break;
            case 5:
                boardArray[5] = symbol;
                break;
            case 6:
                boardArray[6] = symbol;
                break;
            case 7:
                boardArray[7] = symbol;
                break;
            case 8:
                boardArray[8] = symbol;
                break;
        }
    }
    //Checks if the game has been completed.
    public static boolean isGameOver(String[] boardArray){
        //Sees if any of the win conditions are won by X. Prints out "You won!" and
        //returns true.
        if(boardArray[0] == "X" && boardArray[1] == "X" && boardArray[2] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[3] == "X" && boardArray[4] == "X" && boardArray[5] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[6] == "X" && boardArray[7] == "X" && boardArray[8] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[0] == "X" && boardArray[3] == "X" && boardArray[6] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[1] == "X" && boardArray[4] == "X" && boardArray[7] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[2] == "X" && boardArray[5] == "X" && boardArray[8] == "X") {
            System.out.println("You won!");
            return true;
        }
        if(boardArray[2] == "X" && boardArray[4] == "X" && boardArray[6] == "X") {
            System.out.println("You won!");
            return true;
        }

        if(boardArray[0] == "X" && boardArray[4] == "X" && boardArray[8] == "X") {
            System.out.println("You won!");
            return true;
        }

        //Sees if any of the win conditions are won by O. Prints out "Computer wins." and
        //returns true.

        if(boardArray[0] == "O" && boardArray[1] == "O" && boardArray[2] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[3] == "O" && boardArray[4] == "O" && boardArray[5] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[6] == "O" && boardArray[7] == "O" && boardArray[8] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[0] == "O" && boardArray[3] == "O" && boardArray[6] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[1] == "O" && boardArray[4] == "O" && boardArray[7] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[2] == "O" && boardArray[5] == "O" && boardArray[8] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        if(boardArray[2] == "O" && boardArray[4] == "O" && boardArray[6] == "O") {
            System.out.println("Computer wins.");
            return true;
        }
        //If all the spots have been taken up, the game ends in a tie. NOTE: This part
        //does not currently work.
        if (!(boardArray[0] != "0" && boardArray[1] != "1" && boardArray[2] != "2" 
        && boardArray[3] != "3" && boardArray[4] != "4" && boardArray[5] != "5"
        && boardArray[6] != "6" && boardArray[7] != "7" && boardArray[8] != "8")){
            System.out.println("Tie.");
            return true;
        }
        //If none of the above if statements return true, this returns false.
        return false;
    }
}