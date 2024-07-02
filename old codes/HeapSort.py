class Heap:
    def __init__(self, arr):
        self.size = len(arr)

    def parent(self, i):
        return int(i-1/2)

    def lchild(self, i):
        return (2*i)+1

    def rchild(self, i):
        return (2*i)+2

    def heapify(self, arr, i):
        largest = i
        l = self.lchild(i)
        r = self.rchild(i)
        if l < self.size and arr[l] > arr[i]:
            largest = l
        if r < self.size and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = swap(arr[i], arr[largest])
            self.heapify(arr, largest)

    def build_heap(self, arr):
        for i in range(int( self.size/2)-1, -1, -1):
            self.heapify(arr, i)


def swap(a, b):
    return b, a


def heap_sort(heap, arr):
    heap.build_heap(arr)
    for i in range(heap.size):
        arr[0], arr[heap.size-1] = swap(arr[0], arr[heap.size-1])
        heap.size = heap.size-1
        heap.heapify(arr, 0)


n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array")
for i in range(n):
    arr.append(int(input()))

heap = Heap(arr)
heap_sort(heap, arr)
print(arr)