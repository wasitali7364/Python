from pathlib import Path

# create directory and sub directory path
monthly_sub_dir = Path.home() / 'Documents/notes/plans/monthly'
yearly_sub_dir = Path.home() / 'Documents/notes/plans/yearly'

monthly_sub_dir.mkdir(parents=True,exist_ok=True)
yearly_sub_dir.mkdir(parents=True,exist_ok=True)

print(f'monthly folder exist : {monthly_sub_dir.exists()}\nyearly folder eixist : {yearly_sub_dir.exists()}')

notes_dir = Path.home() / 'Documents/notes/plans'

# iterating over path
for path in notes_dir.iterdir():
    print(path)


r'''
    Output:
    C:\Users\wasit.ali.CORP\Documents\notes\plans\monthly
    C:\Users\wasit.ali.CORP\Documents\notes\plans\yearly
'''
print('-------------------------------------------------------')

# create file
read_me = notes_dir / 'readme.md'
read_me.touch()

# iterating over path
for path in notes_dir.iterdir():
    print(path)


r'''
    Output:
    C:\Users\wasit.ali.CORP\Documents\notes\plans\monthly
    C:\Users\wasit.ali.CORP\Documents\notes\plans\yearly
    C:\Users\wasit.ali.CORP\Documents\notes\plans\readme.md
'''
print('-------------------------------------------------------')