
# Creating a stack
def createStack():
    stack = []
    return stack


# Creating an empty stack
def checkEmpty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (checkEmpty(stack)):
        return "stack is empty"

    return stack.pop()


stack = createStack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("stack after popping an element: " + str(stack))

print("popped item: " + pop(stack))

