import hashlib

input_data = input()
result = hashlib.sha256(input_data.encode()).hexdigest()
print(result)