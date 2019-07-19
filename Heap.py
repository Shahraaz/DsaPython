class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.Heap = [0]*self.HEAP_SIZE
        self.currPosisition = -1

    def isFull(self):
        return self.currPosisition == self.HEAP_SIZE

    def insert(self, item):
        if self.isFull():
            print("Heap is Full")
            return
        self.currPosisition += 1
        self.Heap[self.currPosisition] = item
        self.fixup(self.currPosisition)

    def fixup(self, index):
        parent = int((index-1)/2)
        while parent >= 0 and self.Heap[parent] < self.Heap[index]:
            temp = self.Heap[index]
            self.Heap[index] = self.Heap[parent]
            self.Heap[parent] = temp
            parent = int((index-1)/2)

    def heapSort(self):
        for i in range(0, self.currPosisition+1):
            temp = self.Heap[0]
            print(temp)
            self.Heap[0] = self.Heap[self.currPosisition - i]
            self.Heap[self.currPosisition - i] = temp
            self.fixDown(0, self.currPosisition-i-1)

    def fixDown(self, index, upto):
        while index <= upto:
            left = 2*index+1
            right = 2*index+2
            if left < upto:
                childtoSwap = None
                if right > upto:
                    childtoSwap = left
                else:
                    if self.Heap[left] > self.Heap[right]:
                        childtoSwap = left
                    else:
                        childtoSwap = right
                if self.Heap[index] < self.Heap[childtoSwap]:
                    temp = self.Heap[index]
                    self.Heap[index] = self.Heap[childtoSwap]
                    self.Heap[childtoSwap] = temp
                index = childtoSwap
            else:
                break


if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(-10)
    heap.insert(0)
    heap.insert(20)
    heap.heapSort()