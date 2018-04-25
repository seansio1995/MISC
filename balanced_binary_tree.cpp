class Solution{
public:
  bool isBalancedTree(TreeNode *root)
  {
    return findDepth(root)==-1 ? false : true;
  }


  int findDepth(TreeNode *root)
  {
    if (!root) return 0;

    int leftDepth=findDepth(root->left);
    if (leftDepth==-1)  return -1;

    int rightDepth=findDepth(root->right);
    if (rightDepth==-1)  return -1;

    if (abs(leftDepth-rightDepth) > 1) return -1;

    return max(leftDepth,rightDepth)+1


  }
}
