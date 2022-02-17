"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.queue = {i: [] for i in range(11)}  # Для очереди можно использовать python dict.

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param priority: priority of element in queue
        :param elem: element to be added
        :return: Nothing
        """
        self.queue[priority].append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for i in range(11):
            if len(self.queue[i]) > 0:
                return self.queue[i].pop(0)
        return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param priority: priority of element in queue
        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if len(self.queue[priority]) > 0:
            return self.queue[priority][ind]
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue = {i: [] for i in range(11)}
        return None
