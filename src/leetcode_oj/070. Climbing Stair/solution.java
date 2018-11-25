import java.util.Arrays;

/**
 * Created by shao on 2018/11/25.
 */
public class solution {
    class Solution {
//        private int[] nums;
//
//        int climbWays(int n){
//            if (n==0||n==1){
//                return 1;
//            }
//            if (nums[n]==-1)
//                nums[n]=climbWays(n-1)+climbWays(n-2);
//            return nums[n];
//        }
//
//        public int climbStairs(int n) {
//            nums = new int[n+1];
//            Arrays.fill(nums, -1);
//            climbWays(n);
//        }
        public int climbStairs(int n){
            int[] nums = new int[n+1];
            Arrays.fill(nums, -1);
            nums[0]=1;
            nums[1]=1;
            for (int i = 2;i<n+1;i++){
                nums[i]=nums[i-1]+nums[i-2];
            }
            return nums[n];
        }
    }
}
