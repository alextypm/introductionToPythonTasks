
index = ["Hello", "Cool"]   # Here we have an index. It is a list
try:
    index_value = int(input())
    element = index[index_value]
    print(element)
except IndexError:
    print("Your number is not in the index.")

