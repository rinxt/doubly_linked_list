from .obj_list import ObjList
from .exceptions import InvalidObjectTypeError

class LinkedList:
    """Класс, представляющий двусвязный список."""

    def __init__(self):
        """Инициализация пустого списка."""
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """Добавляет новый объект в конец списка."""
        if not isinstance(obj, ObjList):
            raise InvalidObjectTypeError()

        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj

    def remove_obj(self):
        """Удаляет последний объект из списка."""
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

    def get_data(self):
        """Возвращает список данных всех узлов."""
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list