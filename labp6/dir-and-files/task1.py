import os
path = 'C:\Users\user\Desktop\pp2_umit\labp6\dir-and-files'
print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nFiles:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
