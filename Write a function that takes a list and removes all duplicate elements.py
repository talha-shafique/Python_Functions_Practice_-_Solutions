def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print(f"List after removing duplicates: {result}")
