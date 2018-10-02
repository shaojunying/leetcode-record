/**
 * Created by shao on 2018/9/5.
 */
public class 最长回文字符串 {

    static class Solution {
        //        注意:此处的p指的是半径,包含自身,也就是最小值为1
        String longestPalindrome(String s) {

//            Manacher算法

//            StringBuffer stringBuffer = new StringBuffer("@");
//            for (int i = 0; i < s.length(); i++) {
//                stringBuffer.append("#");
//                stringBuffer.append(s.charAt(i));
//            }
//            stringBuffer.append("#");
//            String string = stringBuffer.toString();
//            System.out.println(string);
//
//            int[] p = new int[string.length()];
//            p[0] = 1;
//
////            记录边界最靠右的回文字符串的中心点和右边界
//            int mostRightPalindromeMiddlePoint = 1;
//            int mostRightPalindromeRightPoint = 0;
//
//
////            记录最大回文字符串的中心点和右边界
//            int maxPalindromeMiddlePoint = 1;
//            int maxPalindromeRightPoint = 0;
//
//            for (int i = 1; i < string.length(); i++) {
////                记录i关于最大回文字符串中心的对称节点
//                int j = 2 * mostRightPalindromeMiddlePoint - i;
//
//                p[i] = mostRightPalindromeRightPoint <= i ? 1 : Math.min(mostRightPalindromeRightPoint - i+1,p[j]);
//
//
//                while (i + p[i] < string.length() && string.charAt(i+p[i])==string.charAt(i-p[i])){
//                    p[i]++;
//                }
//
//
////                当前右边界大于最大右边界
//                if (i+p[i] -1 > mostRightPalindromeRightPoint){
//                    mostRightPalindromeMiddlePoint = i;
//                    mostRightPalindromeRightPoint = i+p[i] -1;
//                }
////                当前长度大于最长长度
//                if (p[i] - 1 > maxPalindromeRightPoint - maxPalindromeMiddlePoint){
//                    maxPalindromeMiddlePoint = i;
//                    maxPalindromeRightPoint = i + p[i]-1;
//                }
//
//            }
//
//
//            String result = (String) string.subSequence(maxPalindromeMiddlePoint*2-maxPalindromeRightPoint,maxPalindromeRightPoint);
//            result = result.replace("#","");
//
//            return result;


//            暴力算法
//            int start = 0;
//            int len = 0;
//            for (int i = 0; i < s.length(); i++) {
//                for (int j = i; j < s.length(); j++) {
//                    int k = i;
//                    for (k = i;k <= (i+j)/2; k++){
//                        if (s.charAt(k) != s.charAt(i+j-k)){
//                            break;
//                        }
//                    }
//                    if (k > (i+j)/2 && j-i+1 > len){
//                        len = j - i + 1;
//                        start = i;
//                    }
//                }
//            }
//            return (String) s.subSequence(start,start+len);


//            动态规划(此代码运行超时

//            if (s.length() == 0){
//                return "";
//            }
//
//            boolean[][] p = new boolean[s.length()][s.length()];
//            int start = 0;
//            int maxLen = 1;
//            for (int i = 0; i < s.length();i++){
//                p[i][i] = true;
//                if (i < s.length()-1&& s.charAt(i) == s.charAt(i+1)){
//                    p[i][i+1] = true;
//                    start = i;
//                    maxLen = 2;
//                }
//            }
//            for (int len = 3;len <= s.length(); len++){
//                for (int i = 0;i <= s.length()-len;i++){
//                    for (int j = i+len-1;j < s.length();j++){
//                        if (p[i+1][j-1]&&s.charAt(i) == s.charAt(j)){
//                            p[i][j] = true;
//                            maxLen = len;
//                            start = i;
//                        }
//                    }
//                }
//            }
//
//            System.out.println(start+"    "+maxLen);
//
//            return (String) s.subSequence(start,start+maxLen);

////            中心扩展的方法
//            int start = 0;
//            int maxLen = 0;
//            for (int i = 0;i < s.length();i++){
//                int len1 = maxLen(s,i,i);
//                int len2 = maxLen(s,i,i+1);
//                int len = Math.max(len1,len2);
//                if (len > maxLen){
//                    maxLen = len;
//                    start = i-(len+1)/2 +1;
//                }
//            }
//            return (String) s.subSequence(start,start+maxLen);
//
//        }
//
////        此函数计算i,j分别向左右走,一直到不是回文子串
//        int maxLen(String s,int i,int j){
//            while (i > -1 && j < s.length() && s.charAt(i) == s.charAt(j)){
//                i--;
//                j++;
//            }
//            return j-i-1>0?j-i-1:0;
//        }

////            运行时间最短的解法
            if (s.length() <=1) return s;
            int[] p = new int[]{0, 1};
            for (int i = 0; i < s.length(); i++) {
                i = helper(s,i,p);
            }
            return (String) s.subSequence(p[0],p[1]);
        }

//        此函数将会以i为中心求最长的回文子串,大于原来的时候将会更新p
//        次函数将会返回新的i值
        private int helper(String s, int i, int[] p) {
            int high = i;
            int low = i;
//            经此循环之后,high将指向最后一个等于s[i]的字符
            while (high+1<s.length()&&s.charAt(low) == s.charAt(high+1)){
                high++;
            }
//            此处记录high的值,下一轮循环直接从此处开始
            i = high;
//经此循环之后high将指向回文串右边的第一个字符
            while (high < s.length() && low > -1 && s.charAt(low) == s.charAt(high)){
                high++;
                low--;
            }

            if (high - low - 1 > p[1]-p[0]){
                p[0] = low +1;
                p[1] = high;
            }
            return i;
        }
//
//    public static String longestPalindrome1(String s) {
//        int maxLength = 0;
//        String maxSubString = "";
//        if (s != null) {
//            maxSubString = s.substring(0, 1);
//            for (int i = 0; i < s.length(); i++) {
//                maxLength = 1;
//                int small = i - 1;
//                int large = i + 1;
//
//                while (small >= 0 && s.charAt(small) == s.charAt(i)) {
//                    maxLength++;
//                    if (maxLength > maxSubString.length()) {
//                        maxSubString = s.substring(small, i + 1);
//                    }
//                    small--;
//                }
//                while (large < s.length() && s.charAt(large) == s.charAt(i)) {
//                    maxLength++;
//                    if (maxLength > maxSubString.length()) {
//                        maxSubString = s.substring(i, large + 1);
//                    }
//                    large++;
//                }
//
//
//                while (small >= 0 && large < s.length()) {
//                    if (s.charAt(small) == s.charAt(large)) {
//                        maxLength = maxLength + 2;
//                        if (maxLength > maxSubString.length()) {
//                            maxSubString = s.substring(small, large + 1);
//                        }
//                    } else {
//                        if (maxLength > maxSubString.length()) {
//                            maxSubString = s.substring(small, large);
//                        }
//                        break;
//                    }
//                    small--;
//                    large++;
//                }
//            }
//        }
//        return maxSubString;
//    }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome("abbbbabbbbbc"));
    }

}
