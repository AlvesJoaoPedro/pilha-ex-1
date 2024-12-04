from pilhaencadeada import PilhaException, Stack

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s)

print(s.subtop()) #subtop = 2

s.desempilha_n(2) 
print(s) # s = [1]

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)


print(stack.obtemBase())