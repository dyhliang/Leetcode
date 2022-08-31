Rewrote solution to use heaps instead:

-Use a hash table to store the occurrences of each value in the original nums list.

-Iterate through the non duplicates collection and utilize heappush to store (-1 * occurrences of the value, value) into a max heap. 

-Loop through k times to heappop the value at index 1 of the tuple above onto res.
