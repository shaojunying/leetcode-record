/**
 * Created by shao on 2018/10/3.
 */
public class 至少是其他数字两倍的最大数 {
    static class Solution {
        int dominantIndex(int[] nums) {
            int maxNum = 0;
            int secondMaxNum = 0;
            int maxI = -1;
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] > maxNum){
                    secondMaxNum = maxNum;
                    maxNum = nums[i];
                    maxI = i;
                }else if (nums[i] > secondMaxNum){
                    secondMaxNum = nums[i];
                }
            }
            if (secondMaxNum * 2 <= maxNum){
                return maxI;
            }
            return -1;
        }
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.dominantIndex(new int[]{1,2,3,4}));
    }
}
