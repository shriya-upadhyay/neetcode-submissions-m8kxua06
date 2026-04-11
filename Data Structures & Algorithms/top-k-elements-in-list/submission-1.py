import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0

            freq_dict[num] +=1

        heap = []

        for key, val in freq_dict.items():
            pair = (val, key)
            heapq.heappush(heap, pair)

            if len(heap) > k:
                heapq.heappop(heap)


        output = []

        for i in range(k):
            top_pair = heapq.heappop(heap)
            output.append(top_pair[1])

        return output





        
        
        