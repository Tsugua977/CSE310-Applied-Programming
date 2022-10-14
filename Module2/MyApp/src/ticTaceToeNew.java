import java.util.*;
import java.util.random.*;
import javax.print.DocFlavor.STRING;

public class ticTaceToeNew {

    static void printBoard(String[] boardArray) 
    {
        System.out.println("| " + boardArray[0] + " | " + boardArray[1] + " | " + boardArray[2] + " |");
        System.out.println("| - | - | - |");
        System.out.println("| " + boardArray[3] + " | " + boardArray[4] + " | " + boardArray[5] + " |");
        System.out.println("| - | - | - |");
        System.out.println("| " + boardArray[6] + " | " + boardArray[7] + " | " + boardArray[8] + " |");
    }
        
    public static void main(String[] args) throws Exception {
        
        String[] boardArray = {"1","2","3","4","5","6","7","8","9"};

        String winner = "none";
        printBoard(boardArray);
        while (winner == "none"){
            

            Scanner player1 = new Scanner(System.in);
            System.out.println("Pick a number from 1-9 to place your X:");

            int boardSpot = player1.nextInt();
            boardSpot -= 1;

            String boardSpotStr = String.valueOf(boardSpot);
            for (int i = 0; i < boardArray.length ; i++) {
            if (boardSpotStr.equals(boardArray[i]) ){
                System.out.println("Found it.");
                break;
            }else{
                System.out.println("Not found.");
            }
            }

            int playerPos = boardSpot;

            placementXO(boardArray, playerPos, "user");
            
            Random randNum = new Random();
            int computerPos = randNum.nextInt(9);
            computerPos -= 1;
            
            placementXO(boardArray, computerPos, "computer");

            printBoard(boardArray);
        }
    }

    public static void placementXO(String[] boardArray, int pos, String player){
        String symbol = "X";
        if (player == "user"){
            symbol = "X";
        } else if (player == "computer"){
            symbol = "O";
        }

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
}

//int[] boardInt = Arrays.stream(boardArray).mapToInt(Integer::parseInt).toArray();

            //int index = Arrays.binarySearch(boardInt, boardSpot);

            //if (index < 0)
            //{
            //System.out.println("found it");
            //}else {
                //System.out.println("not in array");
            //}