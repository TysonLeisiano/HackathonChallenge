# Read a list of integers from the console
input_string = input("Enter your integers(separate by commas): ")

# Convert the input string into a list of integers
numbers = list(map(int, input_string.split()))

# Remove duplicates by converting the list to a set
duplicates = list(set(numbers))

# Sort the list in descending order
duplicates.sort(reverse=True)
# Print the sorted list
print("no duplicates list:", duplicates)
