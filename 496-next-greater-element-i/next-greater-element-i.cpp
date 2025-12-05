class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
       int n=nums2.size();
        vector<int> ans(*max_element(nums2.begin(),nums2.end())+1);
        stack<int> st;
        for (int i=n-1;i>=0;i--){ 
            while(!st.empty() && st.top()<=nums2[i]){
                 st.pop();
            }
            ans[nums2[i]]=st.empty()?-1:st.top();
            st.push(nums2[i]);

        }
        vector<int> v;
        for( int i: nums1){
            v.push_back(ans[i]);
        }
        return v;

    }
};