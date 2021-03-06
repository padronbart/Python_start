class Tree:
    '''Estructura anstracta para la definicon de un arbol'''

    class Position:
        '''Posicion de cada elemento'''
        def element(self):
            '''Returna el valor del elemento en esta posicion'''
            raise NotImplementedError('Debe ser implementado por una subclase')

        def __eq__(self, other):
            '''Retuna true si otro elemento representa la misma posicion'''
            raise NotImplementedError('Debe ser implementado por una subclase')

        def __neg__(self, other):
            '''Retorna true si otro elmento no representa la misma poscion'''
            return not(self == other)

    def root(self):
        '''Retorna la posicion que representa el root'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def parent(self, p):
        '''Representa la poscion representada por el padre'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def numChildren(self,p):
        '''Retorna el numero de hijos q p tiene'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def children(self,p):
        '''Genera una iteracion de lo hijos q p tiene'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def __len__(self):
        '''Retoran el numero de elementos contenidos en el tree'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def is_root(self,p):
        '''Retorna true si la posicion p representa la poscion  del root'''
        return self.root() == p

    def is_leaf(self,p):
        '''Retorna true si la posicon p no tiene hijos'''
        return self.numChildren(p) == 0

    def is_empty(self):
        '''Retorna true si el arbol esta vacio'''
        return len(self) == 0


class BinaryTree(Tree):
    '''Clase abstracta de una etrucutra de arbol binario'''
    def left(self, p):
        '''Retorna la posicion del hijo izquierdo'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def right(self, p):
        '''Retorna la posicion del hijo derecho'''
        raise NotImplementedError('Debe ser implementado por una subclase')

    def sibiling(self,p):
        '''Retorna la posicion de un familiar'''
        parent = self.parent(p)
        if parent is None:
            return  None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        '''Genera una iteracion de posciones representando los hijos de p'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(o)