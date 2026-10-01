# list_warmup.py

# Create a list with four fruits
fruits = ["apple", "banana", "cherry", "date"]

# Print the first and the last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Append a fifth fruit and print the whole list
fruits.append("elderberry")
print("List after append:", fruits)

# Remove one fruit and print the list again
fruits.remove("banana")
print("List after remove:", fruits)

# Print how many fruits remain using len()
print("Remaining number of fruits:", len(fruits))
