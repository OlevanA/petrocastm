import os
import shutil

# Paths
desktop_path = r"C:\Users\oleva\OneDrive - Høgskolen i Innlandet\Desktop"  # Your Desktop path
destination_folder = r"C:\Users\oleva\OneDrive - Høgskolen i Innlandet\Desktop\Test PDF"  # Destination folder

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move PDF files
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)
    if os.path.isfile(item_path) and item.lower().endswith('.pdf'):
        shutil.move(item_path, os.path.join(destination_folder, item))
        print(f"Moved: {item}")

print("All PDFs have been moved!")
