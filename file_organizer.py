import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]

            new_folder = os.path.join(folder_path, ext)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(file_path, os.path.join(new_folder, filename))

    print("Files organized!")

if __name__ == "__main__":
    path = input("Enter folder path: ")
    organize_files(path)
