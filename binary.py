# 二分查找法的实现
# 时间复杂度 O(log n)

import time

def binary_search(list,item):
	low = 0;
	high = len(list) - 1
	while low <= high:
		mid = int((low + high) / 2)
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

def main():

	mList = []
	for i in range(100000):
		mList.append(i)
	item = 67898
	start = time.perf_counter()
	print(binary_search(mList,item))
	print(time.perf_counter() - start)

main()