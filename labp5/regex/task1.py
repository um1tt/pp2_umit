import re

pattern = r'a(b*)'
text = input("Enter a string: ")
if re.fullmatch(pattern, text):
    print("YES")
else:
    print("NO")
