from pathlib import Path
import shutil

yearly_dir = Path.home() / 'Documents/notes/plans/yearly'

# check if dir exists
print(yearly_dir.exists()) # True

# print list of files in yearly_dir
print(list(yearly_dir.iterdir()))
# [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/yearly/2033.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/yearly/2034.txt')]

# delete entire folder
shutil.rmtree(yearly_dir)

# check if folder deleted successfully
print(yearly_dir.exists()) # False

# check if any file inside yearly_dir is available
print(list(yearly_dir.rglob("*[34].txt"))) # []