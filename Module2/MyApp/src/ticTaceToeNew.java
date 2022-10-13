import java.util.*;

public class ticTaceToeNew {

    public class Tic_Tac_Toe {

        //char[] [] boardArray = new char [3] [3];
        static int boardArray[] = {1,2,3,4,5,6,7,8,9};
    
        static void printBoard() 
        {
            System.out.println("| " + boardArray[0] + " | " + boardArray[1] + " | " + boardArray[2] + " |");
            System.out.println("| - | - | - |");
            System.out.println("| " + boardArray[3] + " | " + boardArray[4] + " | " + boardArray[5] + " |");
            System.out.println("| - | - | - |");
            System.out.println("| " + boardArray[6] + " | " + boardArray[7] + " | " + boardArray[8] + " |");
        }
        
        public static void main(String[] args) throws Exception {
            
            String winner = null;
            printBoard();


            Scanner player1 = new Scanner(System.in);
            System.out.println("Pick a number from 1-9 to place your X:");

            int boardSpot = player1.nextInt();
            for (int i=0;i < boardArray.length ; i++)
            {
            if (boardSpot == boardArray[i])
            {
            System.out.println("found it");
            break;
            }else {
                System.out.println("not in array");
            }
            }

        }
    }
}