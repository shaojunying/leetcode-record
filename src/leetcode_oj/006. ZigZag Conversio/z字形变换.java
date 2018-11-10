/**
 * Created by shao on 2018/9/6.
 */
public class z字形变换 {

    static class Solution {
        String convert(String s, int numRows) {


////            解法1:找每一列的规律,列出表达式进行计算,遍历次数小于n
//
////            如果numRows为1的时候,直接return原字符串
//            if (numRows == 1){
//                return s;
//            }
//
//
//
//            StringBuffer stringBuffer = new StringBuffer();
////            遍历所有的行
//            for (int i = 0; i < numRows; i++) {
//                for (int x=0;(2*numRows-2)*x+i < s.length();x++){
//                    stringBuffer.append(s.charAt((2*numRows-2)*x+i));
//                    if (i != 0 && i != numRows-1 && ((2*numRows-2)*(x+1)-i) < s.length()){
//                        stringBuffer.append(s.charAt((2*numRows-2)*(x+1)-i));
//                    }
//                }
//            }
//            return stringBuffer.toString();

//            和上一个方法基本类似
//            if (s.length() == 1) {
//                return s;
//            }
//
//            // 每一个循环中的元素数量
//            int group = 2*numRows-2;
//            // 创建存储结果的stringbuffer
//            StringBuilder stringBuilder = new StringBuilder();
//
//            // 遍历所有的行,以1开始
//            for (int i = 1;i <= numRows ; i++) {
//                int temp = 2*numRows - 2 * i;
//                if (i == numRows) {
//                    temp = 2*numRows-2;
//                }
//
//                int index = i;
//                while(index <= s.length()){
//                    stringBuilder.append(s.charAt(index-1));
//                    index+=temp;
//                    temp = group - temp;
//                    if(temp == 0){
//                        temp = group;
//                    }
//                }
//            }
//
//            return stringBuilder.toString();

            return "";

        }
    }

    public static void main(String[] args) {

        Solution solution = new Solution();

        System.out.println(solution.convert("PAYPALISHIRING",3));
    }

}
