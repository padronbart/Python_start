
class LinkedList:

    class Node:
        '''Raw class de un nodo para el linked list'''
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Creacion de un linked list vacio'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Retorna la dimension de la lista'''
        return self._size

    def is_empty(self):
        '''Determina si la lista esta vacia'''
        return self._size == 0

    def push(self, e):
        '''Adiciona elmentos a la lista'''
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        '''Retorna el valor de la cabeza del linked list'''
        if self.is_empty():
            print("Vacio")
        return self._head._element

    def pop(self):
        '''Elimina el elmento pricipal de la lista'''
        if self.is_empty():
            print("Vacio")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer