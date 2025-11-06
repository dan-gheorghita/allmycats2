```python
# Initialize an empty list to store cat names
catNames = []

# Enter an infinite loop to continuously ask for cat names
while True:
    # Prompt the user to enter the name of a cat
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    # Get the user's input
    name = input()

    # Check if the user wants to stop entering names
    if name == '':
        # If so, break out of the loop
        break

    # Add the user's input to the list of cat names
    catNames = catNames + [name]  # list concatenation

# Print out all the cat names
print('The cat names are:')
# Iterate over each name in the list and print it
for name in catNames:
    print('  ' + name)
```