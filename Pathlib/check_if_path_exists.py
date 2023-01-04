from pathlib import Path

# home dir
home = Path.home()
print(f'{home = }')

# desktop
desk = home / 'Desktop'
print(f'{desk = }')

# documents
docs = home.joinpath('Documents')
print(f'{docs = }')

# check if filepath exist (True/False)
chk_desk = desk / 'test.py'
print(chk_desk.exists())

chk_docs = docs / 'test.py'
print(chk_docs.exists())

# check if path is file or dir (True/False)
print(chk_desk.is_file()) # -> True
print(chk_desk.is_dir()) #  -> False
