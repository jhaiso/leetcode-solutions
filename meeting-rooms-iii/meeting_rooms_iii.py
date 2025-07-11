from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        count = [0] * n
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        ongoing = []  # (end_time, room_number)

        for start, end in meetings:
            # Free up rooms where meetings have ended
            while ongoing and ongoing[0][0] <= start:
                finished_end, room = heapq.heappop(ongoing)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing, (end, room))
            else:
                # All rooms are busy, wait for the earliest to free up
                earliest_end, room = heapq.heappop(ongoing)
                duration = end - start
                new_end = earliest_end + duration
                heapq.heappush(ongoing, (new_end, room))
            count[room] += 1

        # Return the room with the most meetings, break ties by smallest index
        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i
