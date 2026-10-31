class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
            count = 0
            sub_sum = 0
            remainder_counts = {0: 1}

            for num in nums:
                sub_sum +=num

                remainder = sub_sum % k

                if remainder in remainder_counts:
                    count += remainder_counts[remainder]

                remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

            return count