from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self._input = ArrayStack()
        self._output = ArrayStack()

    def __len__(self):
        return len(self._input) + len(self._output)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, val):
        self._input.push(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        if self._output.is_empty():
            while not self._input.is_empty():
                self._output.push(self._input.pop())

        return self._output.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        if self._output.is_empty():
            while not self._input.is_empty():
                self._output.push(self._input.pop())

        return self._output.top()
