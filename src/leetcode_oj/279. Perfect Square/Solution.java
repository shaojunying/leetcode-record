import java.util.Arrays;

/**
 * Created by shao on 2018/12/16.
 */
class Solution {
    public int numSquares(int n) {
        int memo[] = new int[n+1];
        Arrays.fill(memo, Integer.MAX_VALUE);
        memo[0] = 0;
        for (int i = 1;i<n+1;i++){
            for (int j = 1;i-j*j >0;j++){
                memo[i] = Math.min(memo[i],1+memo[i-j*j]);
            }
        }
        return memo[n];
    }
}
