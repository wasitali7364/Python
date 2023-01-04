'''
    Review Exercises
        1. Create a new directory in your home folder called my_folder/
        2. Inside my_folder/ create three files:
            file1.txt
            file2.txt
            imagel.png
        3. Move the file imagel.png to a new directory called images/ inside the
            my_folder/ directory.
        4. Delete the file filel.txt
        5. Delete the my_folder/ directory.
'''

from pathlib import Path
import shutil

my_folder = Path.home() / 'Documents/my_folder'
print(my_folder) # Output -> C:\Users\wasit.ali.CORP\Documents\my_folder

print(my_folder.exists()) # False

# 1.
my_folder.mkdir(exist_ok=True)
# check if path created successfully
print(my_folder.exists()) # True

# 2.
files = ['file1.txt', 'file2.txt', 'image1.png']
for file in files:
    my_file = my_folder / file
    print(my_file)
    my_file.touch(exist_ok=True)

# 3.
image_dir = my_folder / 'images'
image_dir.mkdir(parents=True, exist_ok=True)

old_image_path = my_folder / 'image1.png'
new_image_path = image_dir / 'image1.png'
old_image_path.replace(new_image_path)

# 4.
file1_path = my_folder / 'file1.txt'
file1_path.unlink(missing_ok=True)


# 5.
shutil.rmtree(my_folder)