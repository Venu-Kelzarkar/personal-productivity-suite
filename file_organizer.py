import os
import shutil

def start_file_organizer():
    path = input("Enter folder path: ")

    if not os.path.exists(path):
        print("Invalid path")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]
            folder = os.path.join(path, ext.upper())

            if not os.path.exists(folder):
                os.makedirs(folder)

            shutil.move(file_path, os.path.join(folder, file))

    print("📁 Files organized successfully!")