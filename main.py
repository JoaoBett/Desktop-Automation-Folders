import os

DIR_NAMES = {"uni":["sgi", "p1", "redes", "bd"], "misc":["fotos", "jogos"], "estudos": ["desenv-Web"]}
DESKTOP_PATH = "C:\\Users\\joaog\\Desktop"

#list all files into all_files
all_files = os.listdir(DESKTOP_PATH)

#Files there
is_files_there = any(file not in sum(DIR_NAMES.values(), []) for file in all_files)

other_files = [file for file in all_files if file not in sum(DIR_NAMES.values(), [])]
for file in other_files:
    print(file)

if is_files_there:
    try:    
        # Create directories if there are other files
        for main_dir, sub_dirs in DIR_NAMES.items():
            full_path = os.path.join(DESKTOP_PATH, main_dir)
            os.makedirs(full_path, exist_ok=True)
            for sub_dir in sub_dirs:
                os.makedirs(os.path.join(full_path, sub_dir), exist_ok=True)
                print(f"Directory '{sub_dir}' created under '{main_dir}' at {os.path.join(full_path, sub_dir)}")
    except FileExistsError:
        print(f"The file already exists on {DESKTOP_PATH}.")
else:
    print("No other files present.")