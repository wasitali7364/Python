from pathlib import Path

notes_dir = Path.home() / 'Documents/notes'

# move goals3.txt file from notes/plans/ directory to notes_dir
old_path_goals3 = notes_dir / 'plans/goals3.txt'
print(old_path_goals3.exists())  # True
print(old_path_goals3.is_file()) # True

new_path_goals3 = notes_dir / 'goals3.txt'
print(new_path_goals3.exists())  # False

# to move a file, use .replace(target), if path already exists then it will overwrite
old_path_goals3.replace(new_path_goals3)
print(old_path_goals3.exists())  # False
print(new_path_goals3.exists())  # True