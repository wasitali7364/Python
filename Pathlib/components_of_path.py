from pathlib import Path

"""
Picking Out Components of a Path
The different parts of a path are conveniently available as properties. Basic examples include:
    .name: the file name without any directory
    .parent: the directory containing the file, or the parent directory if path is a directory
    .stem: the file name without the suffix
    .suffix: the file extension
    .anchor: the part of the path before the directories
"""
path = Path.cwd().joinpath('data','text_file.txt')

print(f'\n{path = }\n')
print('\n***********************************************************\n')
print(f'  Name   : {path.name}')
print(f'  Parent : {path.parent}')
print(f'  Stem   : {path.stem}')
print(f'  Suffix : {path.suffix}')
print(f'  Anchor : {path.anchor}')
print('\n***********************************************************\n')

# Output
r"""

***********************************************************

  Name   : text_file.txt
  Parent : C:\Users\wasit.ali.CORP\Downloads\vscode\Pathlib\File_System_Operations\data
  Stem   : text_file
  Suffix : .txt
  Anchor : C:

***********************************************************

"""