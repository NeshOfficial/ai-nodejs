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

import os
import re
import requests

# Define menu categories with their URLs
menu_urls = {
    "Breakfast": "https://mcdonalds.com.pk/full-menu/breakfast/",
    "Beef": "https://mcdonalds.com.pk/full-menu/beef/",
    "Chicken and Fish": "https://mcdonalds.com.pk/full-menu/chicken-and-fish/",
    "Crispy Chicken": "https://mcdonalds.com.pk/full-menu/crispy-chicken/",
    "Wraps": "https://mcdonalds.com.pk/full-menu/wraps/",
    "Happy Meal": "https://mcdonalds.com.pk/full-menu/happy-meal/",
    "Extra Value Meals": "https://mcdonalds.com.pk/full-menu/extra-value-meals/",
    "Value Meals": "https://mcdonalds.com.pk/full-menu/value-meals/",
    "Desserts": "https://mcdonalds.com.pk/full-menu/desserts/",
    "Beverages": "https://mcdonalds.com.pk/full-menu/beverages/",
    "Mc Cafe": "https://mcdonalds.com.pk/full-menu/mccafe/",
    "Fries and Sides": "https://mcdonalds.com.pk/full-menu/fries-and-sides/"
}

# Create a directory to store the menu files
output_dir = "scraped_menus"
os.makedirs(output_dir, exist_ok=True)
print(f"Created directory: {output_dir}")

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

# Loop through each menu category
for category_name, url in menu_urls.items(): authentication
    print(f"Processing category: {category_name}")

    # Fetch the webpage content
    response = requests.get(url)
    webpage_content = response.text

    # Check if the menu category is found on the webpage
    if category_name.lower() in webpage_content.lower():
        # Sanitize the file name by removing special characters
        sanitized_name = re.sub(r'[^A-Za-z0-9]', '', category_name)

        # Extract item names
        extracted_items = re.findall(r'<span class="categories-item-name">([^<]+)</span>', webpage_content)

        # Save the extracted items to a file with line numbers
        output_file = os.path.join(output_dir, f"{sanitized_name}.txt")
        with open(output_file, 'w') as f:
            for idx, item in enumerate(extracted_items, 1):
                f.write(f"{idx}. {item}\n")

        print(f"Successfully saved items for {category_name} to {output_file}")
    else:
        print(f"Warning: {category_name} not found on the webpage.")

 main
