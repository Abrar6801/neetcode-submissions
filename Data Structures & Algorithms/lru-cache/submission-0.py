class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity

        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, newNode):
        temp = self.head.next

        newNode.prev = self.head
        newNode.next = temp

        temp.prev = newNode
        self.head.next = newNode

    def deleteNode(self, delNode):
        prevNode = delNode.prev
        nextNode = delNode.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.value

            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)

            self.m[key] = resNode

            return ans

        return -1

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.m:
            curr = self.m[key]

            del self.m[key]
            self.deleteNode(curr)

        # Cache is full
        if len(self.m) == self.cap:
            lruNode = self.tail.prev

            del self.m[lruNode.key]
            self.deleteNode(lruNode)

        # Add new node to front
        newNode = self.Node(key, value)
        self.addNode(newNode)
        self.m[key] = newNode