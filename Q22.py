str1="Python"
output= [chr(ord(char)-5) for char in str1]
print("".join(output))