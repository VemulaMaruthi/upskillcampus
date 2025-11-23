import os
import shutil

# Define the categories and associated extensions
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.xls', '.csv'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Others'

def organize_folder(source_folder):
    for filename in os.listdir(source_folder):
        if os.path.isdir(os.path.join(source_folder, filename)):
            continue  # Skip directories
        file_path = os.path.join(source_folder, filename)
        category = get_category(filename)
        dest_folder = os.path.join(source_folder, category)
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, filename)
        shutil.move(file_path, dest_path)
        print(f"Moved '{filename}' to '{category}' folder.")

if __name__ == "__main__":
    source = input("Enter the path of the folder to organize: ").strip()
    if os.path.isdir(source):
        organize_folder(source)
        print("Organization complete!")
    else:
        print("The specified folder does not exist.")
