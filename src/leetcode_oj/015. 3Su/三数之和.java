
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
/**
 * Created by shao on 2018/11/10.
 */
public class 三数之和 {

    static class Solution {
        public List<List<Integer>> threeSum(int[] nums) {
//            解法1:首先对i进行遍历,之后,在i后使用双指针法,直到找到目标值

////            给定一个包含 n 个整数的数组 nums，判断 nums 中
//// ·          是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
////            找出所有满足条件且不重复的三元组。
//
//            List<List<Integer>> result = new ArrayList<>();
////            首先需要将nums进行排序
//            Arrays.sort(nums);
////            i从0遍历到倒数第3个元素
//            for (int i = 0; i < nums.length-2; i++) {
//                if (i > 0 && nums[i] == nums[i-1]){
//                    continue;
//                }
////                p从i+1开始,q从n-1开始
//                int p = i +1;
//                int q = nums.length -1;
//                while (p < q){
////                    当前的i p q满足条件
//                    if (nums[p]+nums[q]+nums[i] == 0){
//                        List<Integer> one_result = new ArrayList<>();
//                        one_result.add(nums[i]);
//                        one_result.add(nums[p]);
//                        one_result.add(nums[q]);
//                        result.add(one_result);
//                        p++;
////                        此处是为了避免重复
//                        while (p < nums.length && nums[p] == nums[p-1]){
//                            p++;
//                        }
//                        q--;
//                    }
////                    当前i p q 大于0的时候
//                    else if (nums[p]+nums[q]+nums[i] < 0){
//                        p++;
////                        此处是为了避免重复
//                        while (p < nums.length && nums[p] == nums[p-1]){
//                            p++;
//                        }
//                    }else {
//                        q--;
//                    }
//                }
//            }

//            最优解法
            if (nums.length < 3){
                return Collections.emptyList();
            }
            List<List<Integer>> result = new ArrayList<>();
//            首先需要找出最大最小值和正数数组 负数数组 0数组 同时记录每个数出现的次数
            int minNum = Integer.MAX_VALUE;
            int maxNum = Integer.MIN_VALUE;
            int zeroSize = 0;
            int positiveSize = 0;
            int negativeSize = 0;
            for (int num :nums) {
                if (num < minNum){
                    minNum = num;
                }
                if (num>maxNum){
                    maxNum = num;
                }

                if (num == 0){
                    zeroSize ++;
                }
                else if (num > 0){
                    positiveSize++;
                }
                else if (num < 0){
                    negativeSize++;
                }
            }

//            进行各种情况的判断
//            如果0的个数大于2,需要添加一个全为0的组
            if (zeroSize > 2){
                result.add(Arrays.asList(0,0,0));
            }
//            如果正数的个数等于0或者负数的个数等于0,直接返回即可
            if (positiveSize == 0 || negativeSize == 0){
                return result;
            }
//            缩小正负的最值的范围
            maxNum = maxNum > -2 * minNum ? -2*minNum : maxNum;
            minNum = minNum < -2 * maxNum ? -2*maxNum : minNum;

            int[] positiveNumbers = new int[positiveSize];
            int[] negativeNumbers = new int[negativeSize];
            int[] map = new int[maxNum - minNum+1];
            positiveSize = 0;
            negativeSize = 0;
            for (int num: nums){
                if (num <= maxNum && num >= minNum){
                    if (map[num-minNum]++ == 0) {
                        if (num > 0) {
                            positiveNumbers[positiveSize++] = num;
                        } else if (num < 0) {
                            negativeNumbers[negativeSize++] = num;
                        }
                    }
                }
            }
            Arrays.sort(negativeNumbers,0,negativeSize);
            Arrays.sort(positiveNumbers,0,positiveSize);
//            开始真正的求解
            for (int i = negativeSize-1; i >=0 ; i--) {
                int negativeNumber = negativeNumbers[i];
                int minPositive = (-negativeSize)>>1;
                int basej = 0;
                while (basej < positiveSize && positiveNumbers[basej] < minPositive){
                    basej++;
                }

//                开始正式的遍历
                for (int j = basej;j<positiveSize;j++){
                    int positiveNumber = positiveNumbers[j];
                    int temp = 0-negativeNumber - positiveNumber;
                    if (temp >= negativeNumber && temp <= positiveNumber){
                        if (temp == negativeNumber){
                            if (map[negativeNumber-minNum] >1){
                                result.add(Arrays.asList(negativeNumber,negativeNumber,positiveNumber));
                            }
                        }
                        else if (temp == positiveNumber){
                            if (map[positiveNumber-minNum] > 1){
                                result.add(Arrays.asList(negativeNumber,positiveNumber,positiveNumber));
                            }
                        }
                        else {
                            if (map[temp-minNum] >0){
                                result.add(Arrays.asList(negativeNumber,temp,positiveNumber));
                            }
                        }
                    }else if (temp < negativeNumber){
//                        此处如果不break的话,将会遇到之前已经加入的list,在这里我们保证list一定位于neg和pos之间
                        break;
                    }
                }

            }

            return result;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.threeSum(new int[]{-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0}));
    }

}

