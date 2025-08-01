/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sum=0;
    void inorder(TreeNode* node){
        if(node==NULL){
            return;
        }
        inorder(node->right);
        sum+=node->val;
        node->val =sum ;
        inorder(node->left);
    } 
    TreeNode* convertBST(TreeNode* root) {
        inorder(root);
        return root;
    }
};