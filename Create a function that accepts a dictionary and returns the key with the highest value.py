def key_with_highest_value(d):
   
    return max(d, key=d.get)


a = {'a': 10, 'b': 25, 'c': 18}
result = key_with_highest_value(a)
print(f"The key with the highest value is: {result}")
