class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> numbs;

        for(int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (numbs.find(diff) != numbs.end()) {
                return {numbs[diff], i};
            }
            numbs.insert({nums[i], i});
        }
        return {};
    }
};
