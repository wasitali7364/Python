import pathlib
desktop = pathlib.Path("C:/Users/wasit.ali.CORP/Desktop")
print(desktop) # Output -> C:\Users\wasit.ali.CORP\Desktop

# Get Current Working Directory
print(f'Current Working Directory -> {pathlib.Path.cwd()}')

# Get Users Home Directory
print(pathlib.Path.home())

# Create Path By Joining Parts Using Special Operator /
print(pathlib.Path.cwd() / 'data' / 'text_file.txt')

# Above can be acheived with .joinpath() method
print(pathlib.Path.cwd().joinpath('data','text_file.txt'))


# Reading Files
path = pathlib.Path.cwd().joinpath('data','text_file.txt')
with open(path, mode='r') as fid:
    print(path.read_text()) # Output -> Hello World


"""
Picking Out Components of a Path
The different parts of a path are conveniently available as properties. Basic examples include:

.name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories

"""
path = pathlib.Path.cwd().joinpath('data','text_file.txt')
print(f'Name : {path.name}')
print(f'Parent : {path.parent}')
print(f'Stem : {path.stem}')
print(f'Suffix : {path.suffix}')
print(f'Anchor : {path.anchor}')

"""
Getting List of All Files in A Directory
"""
path = pathlib.Path.cwd().joinpath('data')
for file in path.iterdir():
    print('---------------------------------------------------------------------------------------------------')
    print(f'File Path : {file},\nFile Name : {file.name}\nIs File : {file.is_file()}\nIs Dir : {file.is_dir()}')
    print('---------------------------------------------------------------------------------------------------')

# Another Way of Getting List Of All Files
print(list(path.iterdir()))

"""

    Glob Pattern	        Matches
    *	                    Every item
    *.txt	                Every item ending in .txt, such as notes.txt or hello.txt
    ??????	                Every item whose name is six characters long, such as 01.txt, A-01.c, or .zshrc
    A*	                    Every item that starts with the character A, such as Album, A.txt, or AppData
    [abc][abc][abc]	        Every item whose name is three characters long but only composed of the characters a, b, and c, such as abc, aaa, or cba

"""
cwd = pathlib.Path.cwd()
print(f'{list(cwd.rglob("*.txt"))}') # Only Include Text File in Output


 # Using a comprehension
files = [item for item in cwd.rglob("*") if item.is_file()]
print(f'{files = }')
for file in files:
    print(file)

# Get File Path
from pathlib import Path

script_path = Path( __file__ ).absolute()

print( script_path )

# Get File Directory
from pathlib import Path

script_dir = Path( __file__ ).parent.absolute()

print( script_dir )


# Delete all files in a folder
path = Path(__file__).parent.absolute().joinpath('data','63')
for file in path.iterdir():
    Path(file).unlink()
