from pathlib import Path

# create directory and sub directory path
monthly_sub_dir = Path.home() / 'Documents/notes/plans/monthly'

# create directory and sub directory
monthly_sub_dir.mkdir(parents=True, exist_ok=True)

# create file path
january_file = monthly_sub_dir / 'january.txt'

# check if file path exist
print(january_file.exists())
#   output -> False

# create file
january_file.touch()

# check if file created
print(january_file.exists())
#   output -> True

# check if it is a file
print(january_file.is_file())
#   output -> True


# Note
'''
    We need to create Folder first before creating file.
    if folder doesn't exist, creating file will throw error
'''