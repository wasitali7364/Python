from pathlib import Path

note_dir = Path.home() / 'Documents/notes/'

# search for markdown file
for path in note_dir.glob('*.md'):
    print(path)

# create some more files
plans_dir = Path. home() / "Documents/notes/plans"
paths = [
    plans_dir / 'goals1.txt',
    plans_dir / 'goals2.txt',
    plans_dir / 'yearly' / '2033.txt',
    plans_dir / 'yearly' / '2034.txt',
    plans_dir / 'goals3.txt',
    plans_dir / 'monthly' / 'february.txt',
    plans_dir / 'monthly' / 'march.md'
]
for path in paths:
    path.touch(exist_ok=True)


# filter .txt files in notes directory
print(list(note_dir.glob('*.txt')))
    # output -> [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/goals1.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/goals2.txt')]

# filter files that start with 2 and end with 3 in yearly directory
yearly_dir = plans_dir / 'yearly'
print(list(yearly_dir.glob('2*3.*')))
    # output -> [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/yearly/2033.txt')]

# filter files that start with goals preceding a single character in plans directory
print(list(plans_dir.glob('goals?.*')))
    # or
print(list(plans_dir.glob('?oals?.*')))
    # output -> [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals1.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals2.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals3.txt')]

# filter files that contains two character extension in notes directory
print(list(note_dir.glob('*.??')))
    # output -> [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/readme.md')]

# filter files that matches single character after goals in plans directory
print(list(plans_dir.glob('goals[1234].*')))
    # output -> [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals1.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals2.txt'), WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals3.txt')]

# Note
'''
    Above file matching only works for give directory and not subdirectory
    To search inside sub directory as well
    Use .glob(**/) or using .rglob()
    PFB the example code
'''
print(list(note_dir.glob('**/?oals[12345].*')))
# alternatively (short hand)
print(list(note_dir.rglob('?oals[12345].*')))
'''
    output
    [WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/goals1.txt'), 
        WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/goals2.txt'), 
        WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals1.txt'), 
        WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals2.txt'), 
        WindowsPath('C:/Users/wasit.ali.CORP/Documents/notes/plans/goals3.txt')]
'''