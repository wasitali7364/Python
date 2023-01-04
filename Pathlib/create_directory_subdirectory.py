from pathlib import Path

# ---------------------------------------------------------------------------------------------------------

# Creating Directory

notes_dir = Path.home() / "Documents/notes"
# C:\Users\wasit.ali.CORP\Documents\notes

# check if notes_dir exists
print(notes_dir.exists())
    # output -> False

# create directory
notes_dir.mkdir()

# check if notes_dir exists
print(notes_dir.exists())
    # output -> True

# if create directory again will throw file exists error
# to avoid this pass arguments to mkdir(exist_ok=True)

notes_dir.mkdir(exist_ok=True)

# this is same as
'''
    if not notes_dir.eixsts():
        notes_dir.mkdir()
'''

# ---------------------------------------------------------------------------------------------------------

# Creating a Sub Directory

# if creating a sub folder inside this newly created notes folder will throw file not found error
# we need to pass parameter to mkdir(parent=True, exist_ok=True)
monthly_sub_dir = notes_dir / "plans" / "monthly"
monthly_sub_dir.mkdir(parents=True, exist_ok=True)

# check if sub directory created
print(monthly_sub_dir.exists())
#   output -> True