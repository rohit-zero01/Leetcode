class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key = lambda x:x[0])

        merged = [intervals[0]]

        for start , end in intervals[1:]:
            last = merged[-1][1]

            if start <= last:
                merged[-1][1] = max(last, end)

            else:
                merged.append([start, end])

        return merged



# class Solution:
#     def merge(self, intervals: list[list[int]]) -> list[list[int]]:
#         # Sort intervals based on start time
#         intervals.sort(key=lambda x: x[0])

#         merged = [intervals[0]]

#         for start, end in intervals[1:]:
#             last_end = merged[-1][1]

#             if start <= last_end:
#                 # Overlapping or adjacent intervals: extend the end boundary
#                 merged[-1][1] = max(last_end, end)
#             else:
#                 # Non-overlapping: start a new interval in the result
#                 merged.append([start, end])

#         return merged