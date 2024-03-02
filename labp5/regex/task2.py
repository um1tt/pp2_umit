import re

pattern = r'ab{2,3}'
text = input("Enter a string: ")
if re.fullmatch(pattern, text):
    print("YES")
else:
    print("NO")
