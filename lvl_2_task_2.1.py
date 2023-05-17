from random import randint


def create_list():
  n = 20
  arr = []
  for i in range (n):
    arr.append(randint(-100,100))
  return arr

arr = create_list()


def minimum(arr):
  i = 0
  while i < len(arr) - 1:
    m = i
    j = i + 1
    while j < len(arr):
      if arr[j] < arr[m]:
        m = j
      j += 1
    arr[i],arr[m] = arr[m],arr[i]
    i += 1
  return arr [0]


def maximum(arr):
  i = 0
  while i < len(arr) - 1:
    m = i
    j = i + 1
    while j < len(arr):
      if arr[j] < arr[m]:
        m = j
      j += 1
    arr[i],arr[m] = arr[m],arr[i]
    i += 1
  return arr [- 1]

print(f"{arr}, max = {maximum(arr)}, min = {minimum(arr)}")