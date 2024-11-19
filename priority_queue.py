class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    
    def push(self, item: dict):
        if "priority" not in item:
            raise KeyError("Dict item is missing priority key")
        if "command" not in item:
            raise KeyError("Dict item is missing command key")

        if item["priority"] < 0 or item["priority"] > 10:
            raise ValueError("Priority out of bounds, priority value must be between [0, 10]")

        self.queue.append(item)

    def isEmpty(self):
        return len(self.queue) == 0

    def pop(self):
        if not len(self.queue):
            print("Queue is empty!")
            return

        priority = self.queue[0]["priority"]
        index = 0

        for idx, item in enumerate(self.queue):
            if item["priority"] < priority:
                priority = item["priority"]
                index = idx

        next_in_queue = self.queue.pop(index)

        return next_in_queue

def print_command(msg):
    return print("Priority: {}".format(msg))

def mixed_use_test():
    print("Running mixed use test")
    q = PriorityQueue()
    q.push({"priority": 10, "command": print_command})
    q.push({"priority": 7, "command": print_command})
    q.push({"priority": 7, "command": print_command})
    q.push({"priority": 1, "command": print_command})

    first_element = q.pop()
    first_element["command"](first_element["priority"])

    second_element = q.pop()
    second_element["command"](second_element["priority"])

    q.push({"priority": 0, "command": print_command})

    while(not q.isEmpty()):
        element = q.pop()
        element["command"](element["priority"])

def test_all_same_priority():
    print("Running test with all the same priority")
    q = PriorityQueue()
    q.push({"priority": 7, "command": print_command})
    q.push({"priority": 7, "command": print_command})
    q.push({"priority": 7, "command": print_command})
    q.push({"priority": 7, "command": print_command})

    while(not q.isEmpty()):
        element = q.pop()
        element["command"](element["priority"])

def test_out_of_bounds_lower_priority():
    print("Running test with out of bounds (lower) priority")
    q = PriorityQueue()
    try:
        q.push({"priority": -1, "command": print_command})
    except Exception as err:
        print(err)

def test_out_of_bounds_upper_priority():
    print("Running test with out of bounds (upper) priority")
    q = PriorityQueue()
    try:
        q.push({"priority": 12, "command": print_command})
    except Exception as err:
        print(err)

def test_empty_queue():
    print("Running test with empty queue")
    q = PriorityQueue()
    q.pop()

def test_missing_priority():
    print("Running test with dictionary missing priority")
    q = PriorityQueue()
    try:
        q.push({"command": print_command})
    except Exception as err:
        print(err)

def test_missing_command():
    print("Running test with dictionary missing priority")
    q = PriorityQueue()
    try:
        q.push({"priority": 3})
    except Exception as err:
        print(err)

mixed_use_test()
test_all_same_priority()
test_out_of_bounds_lower_priority()
test_out_of_bounds_upper_priority()
test_empty_queue()
test_missing_priority()
test_missing_command()
