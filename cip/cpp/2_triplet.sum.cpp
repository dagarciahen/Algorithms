#include <iostream>
#include <vector>
#include <algorithm>

using namespace std; 

vector<int> tripletSum(vector<int>& nums){
	sort(nums.begin(), nums.end());
	int n = nums.size();
	vector<vector<int>> triplets;

	for (int i = 0; i < n; i++){
		vector<int> triplet;
		// a+b+c = 0 b+c = -a
		int a = nums[i];
		if (a == 0) break;
		if (i >0 && nums[i] == nums[i+1])continue;
		int target = -a;
		int j = i +1;
		int k = n-1;

		while (j < k){
		
			int b = nums[j];
			int c = nums[k];
			if (b +c < target) j++;
			else if (b +c > target) k--;
			else{
				triplet = {a, nums[j], nums[k]}
				triplets.push_back(triplet);
				while (j < k && nums[j] == nums[j+1]){
					j++;

			}
			}
		}
	}
}
int main(){
	vector<int> nums = {-1, 0, 1,2, -1, -4};
	vector<vector<int>> result = tripletSum(nums);

	for (auto& t: result) {
		cout << "[" << t[0] << ", " << t[1] << ", " << t[2] << "]\n";
	}
	return 0;
}






