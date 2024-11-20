class PriorityQueue(object):
    def __init__(self):
        self._queue = []

    def push(self, item):
        if "priority" not in item:
            raise KeyError("Dict item is missing priority key")
        if "command" not in item:
            raise KeyError("Dict item is missing command key")

        if item["priority"] < 0 or item["priority"] > 10:
            raise ValueError(
                "Priority out of bounds, priority value must be between [0, 10]"
            )

        self._queue.append(item)

    def isEmpty(self):
        return len(self._queue) == 0

    def pop(self):
        if not len(self._queue):
            return None

        priority = self._queue[0]["priority"]
        index = 0

        for idx, item in enumerate(self._queue):
            if item["priority"] < priority:
                priority = item["priority"]
                index = idx

        next_in_queue = self._queue.pop(index)

        return next_in_queue
