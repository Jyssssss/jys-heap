class Heap:
    def __init__(self, iterable):
        self.heap = [item for item in iterable]
        self.heapify()

    def get_size(self):
        return len(self.heap)

    def is_root(self, idx):
        return idx == 0

    def is_leaf(self, idx):
        return self.get_left(idx) > self.get_size()

    def get_parent(self, idx):
        return (idx - 1) // 2

    def get_left(self, idx):
        return 2 * idx + 1

    def get_right(self, idx):
        return 2 * idx + 2

    def heapify(self, idx=None):
        if idx == None:
            for i in range(self.get_size() // 2 - 1, -1, -1):
                self.heapify(i)
        else:
            if not self.is_leaf(idx):
                if self.heap[idx] > self.heap[self.get_left(idx)] or self.get_right(idx) < self.get_size() and self.heap[idx] > self.heap[self.get_right(idx)]:
                    if self.get_right(idx) < self.get_size() and self.heap[self.get_right(idx)] < self.heap[self.get_left(idx)]:
                        self.swap(idx, self.get_right(idx))
                        self.heapify(self.get_right(idx))
                    else:
                        self.swap(idx, self.get_left(idx))
                        self.heapify(self.get_left(idx))

    def push(self, element):
        self.heap.append(element)
        cur = self.get_size() - 1
        while not self.is_root(cur) and self.heap[cur] < self.heap[self.get_parent(cur)]:
            self.swap(cur, self.get_parent(cur))
            cur = self.get_parent(cur)

    def pop(self):
        if self.heap:
            self.swap(0, self.get_size() - 1)
            element = self.heap.pop()
            self.heapify()
            return element

    def swap(self, p, q):
        self.heap[p], self.heap[q] = self.heap[q], self.heap[p]
