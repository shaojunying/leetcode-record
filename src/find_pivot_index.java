/**
 * Created by shao on 2018/10/3.
 */
public class find_pivot_index {
    static class Solution {
        int pivotIndex(int[] nums) {
//            首先计算整个数组的和
            if(nums.length <= 2){
                return -1;
            }
            int sum = 0;
            for (int num : nums){
                sum+=num;
            }
            int sum_right = sum;
            int sum_left = 0;
            for(int i = 0;i < nums.length;i++){
                sum_right -= nums[i];
                if(i >0) {
                    sum_left += nums[i - 1];
                }
                if (sum_left == sum_right){
                    return i;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.pivotIndex(new int[]{-1,-1,-1,1,1,-1}));
    }

}
