import java.util.Arrays;

/**
 * Created by shao on 2018/9/13.
 */
public class 计算两个有序数组的中位数 {
    static class Solution {
        public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            int nums1_length = nums1.length;
            int nums2_length = nums2.length;

            // 我们这里要保证nums1的长度要小于nums2的长度
            if(nums1_length > nums2_length){
                // 交换两个数组
                int[] temp_list = nums1;
                nums1 = nums2;
                nums2 = temp_list;

                int temp = nums1_length;
                nums1_length = nums2_length;
                nums2_length = temp;
            }

//            首先规定i循环的左右边界分别为nums1的左右边界
            int iMin = 0,iMax = nums1_length;
            int halfLen = (nums1_length+nums2_length+1)/2;
//            在这里i和j组合的(不包含i,j)的组合将会正好等于len/2或len/2+1
//            开始进行循环,一直到找到正确的值
            while (iMin<=iMax){
                int i = (iMax+iMin)/2;
                int j = halfLen - i ;
                if (i < iMax && nums2[j-1] > nums1[i]){
//                    i太小了
                    iMin = i+1;
                }else if (i > iMin && nums1[i-1] > nums2[j]){
//                    i太大了
                    iMax = i - 1;
                }
                else {
//                    已经找到合适的i和j的值
//                    计算左边的最大值
                    int leftMax = 0;
                    if (i == 0){
//                        nums1全部大于nums2
                        leftMax = nums2[j-1];
                    }else if (j == 0){
                        leftMax = nums1[i-1];
                    }
                    else {
                        leftMax = Math.max(nums1[i-1],nums2[j-1]);
                    }
                    if ((nums1_length+nums2_length)%2 == 1){
                        return leftMax;
                    }
//                        计算右边的最小值
                    int rightMin = 0;
                    if (i == nums1_length){
                        rightMin = nums2[j];
                    }else if (j == nums2_length){
                        rightMin = nums1[i];
                    }
                    else{
                        rightMin = Math.min(nums1[i],nums2[j]);
                    }
                    return (leftMax+rightMin)/2.0;
                }
            }

            return 0.0;

        }


    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findMedianSortedArrays(new int[]{}, new int[]{1}));
    }


}
