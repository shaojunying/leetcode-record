/**
 * Created by shao on 2018/9/11.
 */
public class 盛最多水的容器 {

    static class Solution {
        public int maxArea(int[] height) {
            int left = 0;
            int right = height.length-1;
            int maxArea = 0;
            while (left<right){
//                左边的长度大于右边
                if (height[left]>height[right]){
                    int area = height[right]*(right-left);
                    maxArea = Math.max(area,maxArea);
                    right--;
                }
                else{
                    int area = height[left] * (right - left);
                    maxArea = Math.max(area,maxArea);
                    left++;
                }
            }
            return maxArea;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));
    }

}
