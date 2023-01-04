from pathlib import Path

file_path = Path.home() / 'Documents/notes/plans/monthly/march.md'

print(file_path.exists()) # True

# To Delete a file use .unlink() method
file_path.unlink()

# check if path deleted successfully
print(file_path.exists()) # False

# Deleting a file which does not exist will throw "File Not Found Error"
# To avoid this error pass argument inside .unlink(missing_ok = True)
file_path.unlink(missing_ok= True)

print(file_path.exists()) # False