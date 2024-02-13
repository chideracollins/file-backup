import os
import shutil
import datetime


def move_folder(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    print(dest_dir)
    try:
        shutil.copytree(source, dest_dir)
        print(f"Your folder has been successfully moved to the new path -> {dest_dir}")
    except FileExistsError:
        print("File path already exists!")

