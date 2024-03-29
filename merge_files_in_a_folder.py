from pathlib import Path
import pandas as pd

# Define the path to the directory containing the data files
data_directory = Path.cwd() / 'Data'

# Get a list of all the files in the directory
file_list = list(data_directory.iterdir())

# Loop through each file and concatenate them into one DataFrame also ignoring empty files
df = pd.concat([pd.read_csv(f) for f in file_list if f.stat().st_size > 1]) # > 1 bytes

# Write the concatenated DataFrame to a new file
df.to_csv('merged_file.csv', index=False)

print("Successfully Merged All The File into One File.")
