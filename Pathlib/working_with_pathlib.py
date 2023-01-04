from pathlib import Path


'''
    Creating Windows Path
'''
# using Strings
path = Path(r'C:\Users\wasit.ali.CORP\Downloads\vscode\Pathlib\File_System_Operations')
print(f'Path = {path} and type is {type(path)}')

# Alternatively
path = Path('C:/Users/wasit.ali.CORP/Downloads/vscode/Pathlib/File_System_Operations')
print(f'Path = {path} and type is {type(path)}')

# using Path.home()
path = Path.home() # --> C:\Users\wasit.ali.CORP
print(f'Path = {path} and type is {type(path)}')

# using Path.cwd()
# --> current working directory (may change during the runtime)
path = Path.cwd()
print(f'Path = {path} and type is {type(path)}')

# using forward slash
path = Path.home() / 'Documents' / 'text.txt'
print(f'Path = {path} and type is {type(path)}')

# Alternatively
path = Path.home().joinpath('Documents','text.txt')
print(f'Path = {path} and type is {type(path)}')