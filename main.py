from doubly_linked_list import *

if __name__ == "__main__":
    lst = LinkedList()

    data1 = "данные 1"
    data2 = "данные 2"
    data3 = "данные 3"

    lst.add_obj(ObjList(data1))
    lst.add_obj(ObjList(data2))
    lst.add_obj(ObjList(data3))

    res = lst.get_data() # ['данные 1', 'данные 2', 'данные 3']

    # try:
    #     lst.add_obj("неправильный объект")
    # except InvalidObjectTypeError as e:
    #     print(f"Ошибка: {e}")

    lst.remove_obj()
    res = lst.get_data() # ['данные 1', 'данные 2']

    lst.remove_obj()
    lst.remove_obj()
    res = lst.get_data() # []
