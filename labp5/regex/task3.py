import re

text = input("Enter a string: ")
pattern = r'\b[a-z]+_[a-z]+\b'
matches = re.findall(pattern, text)
print("Sequences found:")
for seq in matches:
    print(seq)
