import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    "Videos": ['.mp4', '.mkv', '.avi', '.mov'],
    "Music": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.html', '.css'],
    "Others": []
}

def organize_files(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find the correct folder
        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                folder_path = os.path.join(directory, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} → {folder}/")
                moved = True
                break

        # If no matching type, move to 'Others'
        if not moved:
            others_path = os.path.join(directory, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved: {filename} → Others/")

# MAIN FUNCTION
if __name__ == "__main__":
    # Replace with the path you want to organize
    path_to_organize = input("Enter the full path of the directory to organize: ")

    if os.path.exists(path_to_organize):
        organize_files(path_to_organize)
        print("✅ File organization completed!")
    else:
        print("❌ The provided directory does not exist.")
