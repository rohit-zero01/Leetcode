class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # if not arr:
        #     return 0
            
        # no_del = arr[0]
        # one_del = arr[0]
        # max_sum = arr[0]
        
        # for i in range(1, len(arr)):
        #     one_del = max(no_del, one_del + arr[i])
        #     no_del = max(arr[i], no_del + arr[i])
        #     max_sum = max(max_sum, no_del, one_del)
            
        # return max_sum



        no_del = one_del = ans = arr[0]

        for i in range(1, len(arr)):
            v1 = no_del
            v2 = one_del + arr[i]

            one_del = max(v1, v2)
            
            v3 = arr[i]
            v4 = arr[i] + no_del

            no_del = max(v3, v4)

            ans = max(ans, max(one_del, no_del))

        return ans

           

        












