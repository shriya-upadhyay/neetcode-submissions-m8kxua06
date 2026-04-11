import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        heap = stones

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first < second:
                heapq.heappush(heap, -(second-first))

            elif second < first:
                heapq.heappush(heap, -(first-second))

        if heap:
            return -(heapq.heappop(heap))

        else:
            return 0 


        