class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._insertion_id = 0

    def get_left_child(self, index):
        return 2*index + 1
    
    def get_right_child(self, index):
        return 2*index + 2
    
    def get_parent_node(self, index):
        return (index -1) // 2
    
    def isEmpty(self):
        return len(self._queue) == 0
    
    def swap(self, index1, index2):
        self._queue[index1], self._queue[index2] = self._queue[index2], self._queue[index1]
    
    def heapify_ascending(self, index):
        parent_index = self.get_parent_node(index)
        while index > 0 and self._queue[parent_index]["priority"] > self._queue[index]["priority"]:
            # Swap with parent
            self.swap(parent_index, index)
            index = parent_index
    
    def heapify_descending(self, index):
        smallest = index
        left_child = self.get_left_child(index)
        right_child = self.get_right_child(index)

        if left_child < len(self._queue) and self._queue[left_child]["priority"] < self._queue[smallest]["priority"]:
            smallest = left_child

        if right_child < len(self._queue) and self._queue[right_child]["priority"] < self._queue[smallest]["priority"]:
            smallest = right_child
        
        #if the priorities are equal check the ids to see which element was added first
        # a smaller id indicates earlier insertion
        if left_child < len(self._queue) and self._queue[left_child]["priority"] == self._queue[smallest]["priority"]:
            if self._queue[left_child]["id"] < self._queue[smallest]["id"]:
                smallest = left_child
        
        if right_child < len(self._queue) and self._queue[right_child]["priority"] == self._queue[smallest]["priority"]:
            if self._queue[right_child]["id"] < self._queue[smallest]["id"]:
                smallest = right_child

        if smallest != index:
            # Swap with the smallest child
            self.swap(smallest, index)
            self.heapify_descending(smallest)

    def push(self, item):
        if "priority" not in item:
            raise KeyError("Dict item is missing priority key")
        if "command" not in item:
            raise KeyError("Dict item is missing command key")

        if item["priority"] < 0 or item["priority"] > 10:
            raise ValueError("Priority out of bounds, priority value must be between [0, 10]")

        # in order to preserve insertion order add an id, 
        # where larger id indicates later insertion time
        item["id"] = self._insertion_id
        self._insertion_id += 1
        
        self._queue.append(item)
        self.heapify_ascending(len(self._queue) - 1)
    
    def pop(self):
        if not len(self._queue):
            return None
        
        if len(self._queue) == 1:
            element = self._queue.pop()
            #remove the insertion id we added before returning to user
            element.pop("id")
            return element

        # Swap the root with the last element before removing it,
        # then redo the heap
        self.swap(0, len(self._queue) -1)
        element = self._queue.pop() 
        self.heapify_descending(0)

        #remove insertion id we added before returning to user
        element.pop("id")
        return element
