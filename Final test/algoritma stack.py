stack = []
stack.append(10)
stack.append(20)
top = stack.pop()

print("stack:", stack)
print("popped:", top)

size = 6
double_stack = [None] * size
top1 = -1
top2 = size

top1 += 1
double_stack[top1] = 10

top2 -= 1
double_stack[top2] = 99
print("Double stack:", double_stack)




