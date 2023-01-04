from pathlib import Path

notes_dir = Path.home() / 'Documents/notes/'

# moving a weekly folder and its content inside plans directory

source = notes_dir / 'weekly'
print(source.exists()) # True

destination = notes_dir / 'plans/weekly'
print(destination.exists()) # False

# move folder with .replace(destination), This will overwrite all folder if dest. already exists
source.replace(destination)
print(source.exists()) # False
print(destination.exists()) # True