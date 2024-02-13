import schedule
import time
from backup import move_folder

# Please ensure you change the source and destination path before running this code.
source_path = "The folder to be moved path"
dest_path = "Where it is to be stored"

schedule.every().day.at("02:51").do(lambda: move_folder(source_path, dest_path))
while True:
    schedule.run_pending()
    time.sleep(60)
