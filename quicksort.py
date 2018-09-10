import random
def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[0]
		less = []
		greater = []
		for i in arr[1:]:
			if i <= pivot:
				less.append(i)
			else:
				greater.append(i)
		return quicksort(less) + [pivot] + quicksort(greater)


arr = []
for i in range(16):
	arr.append(random.randint(0,100))
print(quicksort(arr))