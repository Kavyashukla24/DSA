class Solution {
public:
    int sum(vector<int>& nums,int d){
        int s=0;
        for(int i=0;i<nums.size();i++){
            s+=ceil((double)(nums[i])/(double)(d));
        }
        return s;

    }
    int smallestDivisor(vector<int>& nums, int threshold) {
        int start=1, end=*max_element(nums.begin(),nums.end()), mid;
        while(start<=end){
            mid=start+(end-start)/2;
            if (sum(nums,mid)<=threshold){
                end=mid-1;
            }
            else{
                start=mid+1;
            }
        }
        return start;
        
    }
};