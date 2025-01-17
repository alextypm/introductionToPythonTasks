# Try block and except -----------------------------------------------------------------------------------
# Define a list named 'index' containing two string elements.
index = ["Hello", "Cool"]

# Start a try block to handle potential errors during user input and list access.
try:
    # Prompt the user to input a number and convert it to an integer.
    index_value = int(input("Enter the index number you want to access: "))

    # Access the element at the specified index in the list.
    element = index[index_value]

    # Print the element retrieved from the list.
    print(element)
except IndexError:
    # Handle the case where the user enters a number outside the range of the list.
    print("Error: Your number is not in the index.")
    # I could also do a except exception that would any error, or could be key or value

# if, elif, Else -----------------------------------------------------------------------------------
# Prompt the user to input an integer value and convert the input to an integer.
value = int(input("Enter an integer: "))

# Check if the input value is less than 10.
if value < 10:
    # If the value is less than 10, print "Hello".
    print("Hello")
# Check if the input value is exactly equal to 10.
elif value == 10:
    # If the value is equal to 10, print "Hello twin".
    print("Hello twin")
# If the value is greater than 10.
else:
    # Print a message for values greater than 10, using a newline character (\n) for formatting.
    print("Hello to you\nBig bro!")

# ---------------------------------------------------------------------------------


