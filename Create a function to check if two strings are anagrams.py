def are_anagrams(str1, str2):
    
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)
