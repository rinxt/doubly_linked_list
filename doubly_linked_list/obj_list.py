class ObjList:
    """Класс, представляющий узел двусвязного списка."""

    def __init__(self, data):
        """Инициализация узла с данными."""
        self.__data = data
        self.__prev = None
        self.__next = None

    # Сеттеры
    def set_next(self, obj):
        """Устанавливает ссылку на следующий узел."""
        self.__next = obj

    def set_prev(self, obj):
        """Устанавливает ссылку на предыдущий узел."""
        self.__prev = obj

    def set_data(self, data):
        """Устанавливает значение данных."""
        self.__data = data

    # Геттеры
    def get_next(self):
        """Возвращает ссылку на следующий узел."""
        return self.__next

    def get_prev(self):
        """Возвращает ссылку на предыдущий узел."""
        return self.__prev

    def get_data(self):
        """Возвращает значение данных."""
        return self.__data