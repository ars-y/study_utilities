class Node:
    """Модель узла."""

    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    """Модель односвязного списка."""

    def __init__(self, iterable=None) -> None:
        self.__head = None
        self.__length = 0

        if iterable:
            if not hasattr(iterable, '__iter__'):
                raise TypeError(
                    '\'%s\' object is not iterable' % type(iterable).__name__
                )
            self.convert(iterable)

    def is_empty(self) -> bool:
        """Проверка пустого списка."""
        return len(self) == 0 and not self.__head

    def __check_index_type(self, index) -> None:
        """Проверка является ли индекс целым числом."""
        if not isinstance(index, int):
            error_message: str = (
                    'linked list indices must be integers, '
                    'not %s' % type(index).__name__
                )
            raise TypeError(error_message)

    def __push(self, item) -> None:
        """Вставка элемента в пустой список."""
        self.__head = Node(item)
        self.__length += 1
        return

    @property
    def first(self):
        """Возвращает значение первого узла из односвязного списка."""
        return self[0].value

    @property
    def last(self):
        """Возвращает значение последнего узла из односвязного списка."""
        return self[len(self) - 1].value

    def convert(self, iterable, reverse=False) -> None:
        """Конвертация итерируемого объекта в односвязный список."""
        if not reverse:
            for item in iterable:
                self.push_back(item)
            return

        for item in iterable:
            self.push_front(item)
        return

    def insert(self, index, item) -> None:
        """
        Вставка элемента в односвязный список до индекса.
        Если индекс нулевой или отрицательный, то элемент идет в начало списка.
        Если индекс превышает количество узлов в односвязном списке,
        то элемент помещает в конец.
        """
        self.__check_index_type(index)

        if self.is_empty():
            self.__push(item)
            return

        if index <= 0:
            self.push_front(item)
            return

        if index >= len(self):
            self.push_back(item)
            return

        node: Node = self[index - 1]
        new_node: Node = Node(item)
        if node.next:
            new_node.next = node.next
        node.next = new_node
        self.__length += 1
        return

    def push_back(self, item) -> None:
        """Вставка элемента в конец односвязного списка."""
        if self.is_empty():
            self.__push(item)
            return

        node: Node = self.__head
        while node.next:
            node = node.next
        node.next = Node(item)
        self.__length += 1
        return

    def push_front(self, item) -> None:
        """Вставка элемента в начало односвязного списка."""
        if self.is_empty():
            self.__push(item)
            return

        node: Node = Node(item, self.__head)
        self.__head = node
        self.__length += 1
        return

    def pop_back(self):
        """Получение элемента из конца списка, с удалением узла."""
        if self.is_empty():
            raise IndexError('pop from empty linked list')

        node: Node = self.__head
        prev_node: Node | None = None
        while node.next:
            prev_node = node
            node = node.next
        item = node.value

        if prev_node:
            prev_node.next = None
        else:
            self.__head = None

        self.__length -= 1
        return item

    def pop_front(self):
        """Получение элемента из начала списка, с удалением узла."""
        if self.is_empty():
            raise IndexError('pop from empty linked list')

        item = self.__head.value
        self.__head = self.__head.next
        self.__length -= 1
        return item

    def reverse(self) -> None:
        """Разворачивает односвязный список."""
        if self.is_empty():
            return

        node: Node | None = None
        while self.__head:
            node = Node(self.__head.value, node)
            self.__head = self.__head.next
        self.__head = node

    def __contains__(self, key) -> bool:
        """Проверка находится ли ключ в односвязном списке."""
        if self.is_empty():
            return False

        node: Node = self.__head
        while node:
            if key == node.value:
                return True
            node = node.next
        return False

    def __getitem__(self, index) -> Node:
        """Получение узла по индексу."""
        self.__check_index_type(index)

        if self.is_empty() or index < 0 or index >= len(self):
            raise IndexError('linked list index out of range')

        it: int = 0
        node: Node = self.__head
        while node.next:
            if it == index:
                return node
            node = node.next
            it += 1
        return node

    def __len__(self) -> int:
        """Возвращает длину односвязного списка."""
        return self.__length

    def __str__(self) -> str:
        if self.is_empty():
            return '[]'

        nodes: list = []
        node: Node = self.__head
        while node:
            nodes.append(node.value)
            node = node.next
        return ', '.join(str(val) for val in nodes)
