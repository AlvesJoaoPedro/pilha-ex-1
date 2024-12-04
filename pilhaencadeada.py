from node import Node

class PilhaException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Stack:

    def __init__(self):
        self.top = None
        self._size = 0
    
    def __str__(self):
        node = self.top
        r = ""
        while(node):    #enquanto não for None
            r = r + str(node.data) + "\n"
            node = node.next #garante que o loop irá acabar 
        return r

    def push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size += 1
    
    def pop(self):
        if self._size > 0:
            self.top = self.top.next
            self._size -= 1
        else:
            raise PilhaException("Pilha index error out of range")
        
    def peek(self):
        if self._size > 0:
            return self.top.data
    
    def subtop(self) -> None:
        if self._size > 0:
            return self.top.next.data
        else:
            raise PilhaException("Pilha não possui subtopo") 
        
    def desempilha_n(self, n : int) -> bool:
        tamanho_inicial = self._size
        if self._size < n:
            raise PilhaException("Números a desempilhar é maior do que o tamanho da pilha.")
        for _ in range(n):
            self.pop()
        return (tamanho_inicial - self._size) == n #retorna true se o pop deu certo, false se não.
    
    def esvaziar(self):
        while self._size != 0:
            self.pop()

    def obtemBase(self):
        if self._size > 0:
            node = self.top
            while node.next: #verifica se o próximo elemento é None (fim da pilha)
                node = node.next
            return node.data
        else:
            raise PilhaException("Pilha vazia.")