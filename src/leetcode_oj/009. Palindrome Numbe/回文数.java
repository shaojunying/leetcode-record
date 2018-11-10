/**
 * Created by shao on 2018/9/6.
 */
public class 回文数 {

    static class Solution {
        public boolean isPalindrome(int x) {
//            不转为字符串解决此问题
//            if (x < 0)
//                return false;
//            int temp = x;
////            此变量将表示x的位数
//            int numTemp = 1;
//            while ((temp=temp/10)!=0){
//                numTemp*=10;
//            }
//
//            while (x != 0){
//                if (x/numTemp!=x%10)
//                    return false;
//                x %= numTemp;
//                x /= 10;
//                numTemp/=100;
//
//            }
//
//            return true;

////            转化为字符串的方法
//            String string1 = String.valueOf(x);
//            String string = new StringBuilder(string1).reverse().toString();
//            return string.equals(string1);

////            将x的最后一半翻转,与前一半进行比较
//            if(x<0 || x%10 == 0 && x != 0){
//                return false;
//            }
//
//            int temp = 0;
//            while(x > temp){
//                temp = temp*10+x%10;
//                x/=10;
//            }
//            return x == temp || x == temp/10;
            return true;
        }
    }

    public static void main(String[] args) {
        System.out.println((new Solution()).isPalindrome(1));
    }
}
