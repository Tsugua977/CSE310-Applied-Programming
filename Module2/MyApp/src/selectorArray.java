public class selectorArray {

    public static void main(String[] args) throws Exception {
        int nums[] = {1,2,3,4,5,6,7,8,9};

        int findMe = 5;

        for (int i=0;i < nums.length ; i++)
        {
        if (findMe == nums[i])
        {
        // found it
        System.out.println("found it");
        break;
        }else {
            System.out.println("not in array");
        // not in array
        }
    }
    }
}