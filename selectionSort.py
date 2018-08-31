# 选择排序
# 时间复杂度O(n*n)

import random
import time

# 从集合中找到最小的那个，返回其索引值
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1,len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
# 将集合中最小的那个取出放入新的集合中
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest_index = findSmallest(arr)
		newArr.append(arr.pop(smallest_index)) 
	return newArr

def main():
	arr = []
	for i in range(100):
		arr.append(random.randint(0,5000))
	print(arr)
	start_time = time.perf_counter()
	print(selectionSort(arr))
	print(time.perf_counter() - start_time)
main()