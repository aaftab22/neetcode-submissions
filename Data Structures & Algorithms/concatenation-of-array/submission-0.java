class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n*2];
        System.out.println("ans length = " + ans.length);
        int k = 0;
        for(int i = 0; i < ans.length; i++){

            if (i < n){
                ans[i] = nums[i];
                System.out.println(ans[i]);
            }

            if (i >= n){
                    ans[i] = nums[k];
                    k++;
                    System.out.println(ans[i]);
            }
        }
        return ans;
    }
}