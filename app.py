#this code is from geekforgeek
from collections import deque

arr = [12, 10, 5, 6, 52, 36]
k = 2

d = deque(arr)
d.rotate(-k)
print(list(d))
