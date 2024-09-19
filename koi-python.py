import string
import random
import os

# Function to generate a difficult file name
def generate_difficult_filename(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to write 50 lines to a file
def write_lines_to_file(filename, num_lines=50):
    with open(filename, 'w') as file:
        for i in range(1, num_lines + 1):
            file.write(f'This is line number {i}\n')

# Generate a difficult file name
difficult_filename = generate_difficult_filename()

# Ensure the file is saved in a safe location
safe_directory = os.path.expanduser('~/difficult_files')
os.makedirs(safe_directory, exist_ok=True)
file_path = os.path.join(safe_directory, difficult_filename)

# Write 50 lines to the file
write_lines_to_file(file_path)

print(f'File with difficult name created at: {file_path}')
