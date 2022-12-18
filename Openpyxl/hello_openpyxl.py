# pip install openpyxl
# https://openpyxl.readthedocs.io/en/stable/


from pathlib import Path
from openpyxl import Workbook 

workbook = Workbook() # Create new Workbook
sheet = workbook.active # Select Active Sheet

sheet['A1'] = 'Hello'
sheet['B1'] = 'World!'

file_path = Path.cwd().joinpath('sample_data','hello_world.xlsx')

workbook.save(filename = file_path)
# The code above should create a file called hello_world.xlsx in the sample_data.