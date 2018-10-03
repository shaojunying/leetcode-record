import java.util.Arrays;

/**
 * Created by shao on 2018/10/3.
 */
public class 加一 {
    public static int[] plusOne(int[] digits) {
        boolean shouldCarry = true;
        for (int i = digits.length-1; i > -1; i--) {
            int temp = digits[i] + 1;
            digits[i] = temp % 10;
            if (temp / 10 == 0) {
                shouldCarry = false;
                break;
            }
        }
        if (shouldCarry){
            digits = new int[digits.length+1];
            digits[0]=1;
        }
        return digits;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(plusOne(new int[]{9})));
    }
}
