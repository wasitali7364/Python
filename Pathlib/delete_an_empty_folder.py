from pathlib import Path

# create an empty folder
daily_dir = Path.home() / 'Documents/notes/plans/daily'
print(daily_dir.is_dir()) # False
daily_dir.mkdir(parents=True, exist_ok=True)

# check if empty folder created
print(daily_dir.is_dir()) # True
'''
    Now Delete This Empty Directory
    To Delete an Empty Directory use .rmdir() which stands for Remove Directory
    .rmdir() only works on Empty Directory
    using .rmdir() on non empty directory will throw OsError explaining that Directory is non Empty
    here is an exampe code to delete empty directory

'''

daily_dir.rmdir()

print(daily_dir.exists()) # False