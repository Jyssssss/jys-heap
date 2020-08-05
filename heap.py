# Implementation of min heap.
class Heap:
    def __init__(self, iterable):
        self.heap = [item for item in iterable]
        self._heapify()

    # Get size of the heap.
    def size(self):
        return len(self.heap)

    # Check is the node of idx is a root or not.
    def _is_root(self, idx):
        return idx == 0

    # Check is the node of idx is a leaf or not.
    def _is_leaf(self, idx):
        return self._left_child(idx) > self.size()

    # Get parent's index.
    def _parent(self, idx):
        return (idx - 1) // 2

    # Get left child's index.
    def _left_child(self, idx):
        return 2 * idx + 1

    # Get right child's index.
    def _right_chid(self, idx):
        return 2 * idx + 2

    # Heapify the node of the given idx.
    # If the idx is not given, _heapify from the root.
    def _heapify(self, idx=None):
        if idx == None:
            for i in range(self.size() // 2 - 1, -1, -1):
                self._heapify(i)
        else:
            if not self._is_leaf(idx):
                if self.heap[idx] > self.heap[self._left_child(idx)] or self._right_chid(idx) < self.size() and self.heap[idx] > self.heap[self._right_chid(idx)]:
                    if self._right_chid(idx) < self.size() and self.heap[self._right_chid(idx)] < self.heap[self._left_child(idx)]:
                        self._swap(idx, self._right_chid(idx))
                        self._heapify(self._right_chid(idx))
                    else:
                        self._swap(idx, self._left_child(idx))
                        self._heapify(self._left_child(idx))

    # Insert an element into the heap.
    def push(self, element):
        self.heap.append(element)
        cur = self.size() - 1
        while not self._is_root(cur) and self.heap[cur] < self.heap[self._parent(cur)]:
            self._swap(cur, self._parent(cur))
            cur = self._parent(cur)

    # Remove the element from the heap, and return it.
    def pop(self):
        if self.heap:
            self._swap(0, self.size() - 1)
            element = self.heap.pop()
            self._heapify()
            return element

    # Retrieve, but not remove, the root of the heap.
    def peek(self):
        if self.heap:
            return self.heap[0]

    # Swap the values of two nodes.
    def _swap(self, p, q):
        self.heap[p], self.heap[q] = self.heap[q], self.heap[p]
