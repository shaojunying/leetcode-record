/**
 * Created by shao on 2018/10/9.
 */
public class 对称二叉树 {
    public class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;

        public TreeNode(int val) {
            this.val = val;

        }

    }
    public class Solution {
        boolean isSymmetrical(TreeNode pRoot)
        {
            return isSymmetrical(pRoot, pRoot);
        }

        boolean isSymmetrical(TreeNode lNode,TreeNode rNode)
        {
            if (lNode == null && rNode == null){
                return true;
            }
            if (lNode == null || rNode == null){
                return false;
            }
            if (lNode.val != rNode.val){
                return false;
            }
            return isSymmetrical(lNode.left,rNode.right)&&isSymmetrical(lNode.right,rNode.left);
        }

    }

}
