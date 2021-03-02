# Bubble sort algorithm

def bubble_sort(num_list):
	for i in range(len(num_list)-1):
		for j in range(i,len(num_list)-1):
			if num_list[j] > num_list[j+1]:
				swap = num_list[j+1]
				num_list[j+1] = num_list[j]
				num_list[j] = swap
	return num_list

num = [32, 50, 13, 96, 70, 154, 87]
num_sort = bubble_sort(num)
print(num_sort)

def bs(a):
	b = len(a)-1 
	for x in range(b):
		for y in range(x,b):
			if a[y] > a[y+1]:
				a[y], a[y+1] = a[y+1], a[y]
	return a

print(bs(num))

num = [32, 50, 13, 96, 70, 154, 87]
num.sort()
print(num)


""" 
QuickSort function takes last element as pivot, places the pivot element at its correct position in sorted array, 
and places all smaller(smaller than pivot) to left of pivot and all greater elements to right of pivot
"""
def partitioning(arr, low, high):
	i = (low-1) # index of smaller element
	print("arr : ", arr,"low :", low,"high :", high)
	pivot = arr[high] # pivot
	for j in range(low, high):
		# if current element is smaller than or equal to pivot 
		if arr[j] <= pivot:
			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

# function to do quick sort
def quickSort(arr, low, high):
	if low < high:
		# pi is partitioning index, arr[p] is now at right place
		pi = partitioning(arr, low, high)
		# separately sort elements before partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("sorted array : ")
for i in range(n):
	print("%d" %arr[i])


























