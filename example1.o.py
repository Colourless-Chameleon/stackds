from stackds import Stack

# Create a new stack
stack = Stack()

# Push items onto the stack
stack.push("Python")
stack.push("Java")
stack.push("C++")
stack.push("JavaScript")

# Display the current stack
print("Current Stack:", stack.display())  # Output: Current Stack: ['Python', 'Java', 'C++', 'JavaScript']

# Peek at the top of the stack
top_item = stack.peek()
print("Top of the Stack:", top_item)  # Output: Top of the Stack: JavaScript

# Search for an item in the stack
search_index = stack.search("Java")
if search_index != -1:
    print(f"'Java' found at index {search_index}")
else:
    print("'Java' not found in the stack")

# Pop items from the stack
popped_item = stack.pop()
print("Popped Item:", popped_item)  # Output: Popped Item: JavaScript

# Display the stack after popping
print("Stack after pop:", stack.display())  # Output: Stack after pop: ['Python', 'Java', 'C++']

# Check if the stack is empty
is_empty = stack.is_empty()
print("Is Stack Empty?", is_empty)  # Output: Is Stack Empty? False

# Pop all items to empty the stack
while not stack.is_empty():
    print("Popped:", stack.pop())

# Final check if the stack is empty
print("Is Stack Empty after all pops?", stack.is_empty())  # Output: Is Stack Empty after all pops? True
