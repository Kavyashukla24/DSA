class Solution {
public:
   vector<int> ncr(int row){
    long long temp=1;
    vector<int> arr;
    arr.push_back(1);
    for(int c=1;c<row;c++){
        temp=temp*(row-c);
        temp=temp/c;
        arr.push_back(temp);
    }
    return arr;
    }

    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i=1;i<=numRows;i++){
            ans.push_back(ncr(i));
        }
        return ans;
    }
};