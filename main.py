import os
import datetime

#Your directories as a dict
DIR_NAMES = {"dir":["subdirs"]}
#Your desktop path
DESKTOP_PATH = "YOUR\\PATH"

all_files = os.listdir(DESKTOP_PATH)

#Files there
is_files = any(file not in sum(DIR_NAMES.values(), []) for file in all_files)

#Weekly Folders
now = datetime.datetime.now()

if is_files:
 for main_dir, sub_dirs in DIR_NAMES.items():
        #Path for the main directory
        full_path = os.path.join(DESKTOP_PATH, main_dir)
        #Create directory
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Directory '{main_dir}' created at {full_path}")
        #Dir already created
        else:
            print(f"The directory '{main_dir}' already exists at {full_path}.")
        
        for sub_dir in sub_dirs:
            #Path for the sub-directories
            sub_full_path = os.path.join(full_path, sub_dir)
            #Create directory
            if not os.path.exists(sub_full_path):
                os.makedirs(sub_full_path)
                print(f"Directory '{sub_dir}' created under '{main_dir}' at {sub_full_path}")
            #Dir already created
            else:
                print(f"The directory '{sub_dir}' already exists under '{main_dir}' at {sub_full_path}.")
else:
    print("No other files present.")