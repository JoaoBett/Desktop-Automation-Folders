import os
import shutil
import time

# Constantes para nomes de diretórios e caminho da área de trabalho
DIR_NAMES = {
    "uni": {
        "1st_year": {
            #"1st_semester": ["analise", "p1", "algebra", "fisica", "sistemas"],
            "2nd_semester": ["p2", "estatistica", "md"]
        },
        "2nd_year": {
            #"1st_semester": ["bd", "redes", "sgi"],
            "2nd_semester": ["ainet","as","rd"]
        },
        #"3rd_year": {
        #    "1st_semester": [],
        #    "2nd_semester": []
        #},
        "Erasmus":{
            "slovenia": ["AdvSecSys", "CompBusiSuc"],
            "Friends": ["photos"],
            "PORTUGAL_University": ["important documents"]
        }
    },
    "misc": ["fotos", "jogos", "random"],
}
DESKTOP_PATH = "C:\\Users\\joaog\\Desktop"

def create_directories(base_path, dir_structure):
    """Creates specified directories and subdirectories if they do not exist."""
    # Create university directories
    university_path = os.path.join(base_path, "uni")
    if not os.path.exists(university_path):
        os.makedirs(university_path)
        print(f"'uni' directory created at {university_path}")
    else:
        print("The 'uni' directory already exists.")

    for year, semesters in dir_structure["uni"].items():
        year_path = os.path.join(university_path, year)
        if not os.path.exists(year_path):
            os.makedirs(year_path)
            print(f"Directory '{year}' created at {year_path}")
        else:
            print(f"The directory '{year}' already exists at {year_path}")

        for semester, sub_dirs in semesters.items():
            semester_path = os.path.join(year_path, semester)
            if not os.path.exists(semester_path):
                os.makedirs(semester_path)
                print(f"Directory '{semester}' created under '{year}' at {semester_path}")
            else:
                print(f"The directory '{semester}' already exists under '{year}' at {semester_path}")

            for sub_dir in sub_dirs:
                sub_full_path = os.path.join(semester_path, sub_dir)
                if not os.path.exists(sub_full_path):
                    os.makedirs(sub_full_path)
                    print(f"Directory '{sub_dir}' created under '{semester}' at {sub_full_path}")
                else:
                    print(f"The directory '{sub_dir}' already exists under '{semester}' at {sub_full_path}")

    # Create misc directories
    for misc_dir in dir_structure["misc"]:
        misc_path = os.path.join(base_path, "misc", misc_dir)
        if not os.path.exists(misc_path):
            os.makedirs(misc_path)
            print(f"Directory '{misc_dir}' created under 'misc' at {misc_path}")
        else:
            print(f"The directory '{misc_dir}' already exists under 'misc' at {misc_path}")


def move_files(base_path, dir_structure):
    """Moves files from the desktop to the appropriate directories."""
    all_files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]
    
    if all_files:
        university_path = os.path.join(base_path, "uni")
        for file in all_files:
            moved = False
            for year, semesters in dir_structure["uni"].items():
                for semester, sub_dirs in semesters.items():
                    for sub_dir in sub_dirs:
                        if sub_dir.lower() in file.lower():
                            source = os.path.join(base_path, file)
                            destination = os.path.join(university_path, year, semester, sub_dir, file)
                            shutil.move(source, destination)
                            print(f"File '{file}' moved to {destination}")
                            moved = True
                            break
                    if moved:
                        break
                if moved:
                    break

            # Check and move files to misc directories
            if not moved:
                for misc_dir in dir_structure["misc"]:
                    if misc_dir.lower() in file.lower():
                        source = os.path.join(base_path, file)
                        destination = os.path.join(base_path, "misc", misc_dir, file)
                        shutil.move(source, destination)
                        print(f"File '{file}' moved to {destination}")
                        moved = True
                        break

            # Check and move files to studies directories
            if not moved:
                for study_dir in dir_structure["estudos"]:
                    if study_dir.lower() in file.lower():
                        source = os.path.join(base_path, file)
                        destination = os.path.join(base_path, "studies", study_dir, file)
                        shutil.move(source, destination)
                        print(f"File '{file}' moved to {destination}")
                        moved = True
                        break


def select_files(base_path, dir_structure):
    """Select where each files goes to."""
    #Scan every file in the base_path
    all_files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]
    file_names = []
    repeated_files = dir_structure.keys()

    #Remove every file that is in the dir_structure
    for file in all_files:
        if file not in repeated_files: 
            file_names.append(file)

    for file in file_names:
        while True:
            folder_options = list(dir_structure.keys())
            print(f"\nWhere should '{file}' be moved?")
            print("\n0: Exit program")
            for idx, folder in enumerate(folder_options, 1):
                print(f"{idx}: {folder}")

            try:
                choice = int(input("Enter the number of the destination folder: ")) - 1

                #Exit Software
                if choice == -1:
                    print("Exiting program...")
                    time.sleep(1)
                    os.sys.exit(0)
                #Display Each Folder Index
                elif 0 <= choice < len(folder_options):
                    destination = folder_options[choice]
                    
                    # Navigate through subfolders
                    final_destination = get_final_destination(destination, dir_structure)
                    print(f"Moving '{file}' to {final_destination}")
                    time.sleep(2.5)
                    os.system("cls")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            
            except ValueError:
                print("ERROR - Invalid destination")

def get_final_destination(base_folder, dir_structure):
    """Navigate through each subfolders until no more folders. """
    current_folder = base_folder
    current_structure = dir_structure[current_folder]  

    while isinstance(current_structure, dict): 
        subfolders = list(current_structure.keys())

        if not subfolders:
            break
        
        #print(f"Subfolders in {current_folder}: {subfolders}")
        print("\n0: Exit program")
        for idx, sub in enumerate(subfolders, 1):
            print(f"{idx}: {sub}")

        try:
            choice = input("\nEnter the number to move inside or press Enter to stay: ").strip()
            if choice == "":
                break
            choice = int(choice) - 1

            #Exit Software
            if choice == -1:
                print("Exiting program...")
                time.sleep(1)
                os.sys.exit(0)
            #Display Each Folder Index
            elif 0 <= choice < len(subfolders):
                current_folder = os.path.join(current_folder, subfolders[choice])
                current_structure = current_structure[subfolders[choice]]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

    return current_folder

def main():
    """Main function to run the script."""
    #create_directories(DESKTOP_PATH, DIR_NAMES)
    select_files(DESKTOP_PATH, DIR_NAMES)
    #move_files(DESKTOP_PATH, DIR_NAMES)

if __name__ == "__main__":
    main()
