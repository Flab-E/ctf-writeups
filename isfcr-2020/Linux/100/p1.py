import hashlib 
str2hash = input()
result = hashlib.md5(str2hash.encode()) 
print(result.hexdigest()) 