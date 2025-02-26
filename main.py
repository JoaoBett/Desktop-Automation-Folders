import os
import shutil

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
    #"studies": ["desenv-Web"]
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

    # Create studies directories
    # for study_dir in dir_structure["estudos"]:
    #     study_path = os.path.join(base_path, "studies", study_dir)
    #     if not os.path.exists(study_path):
    #         os.makedirs(study_path)
    #         print(f"Directory '{study_dir}' created under 'studies' at {study_path}")
    #     else:
    #         print(f"The directory '{study_dir}' already exists under 'studies' at {study_path}")

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
    repeated_files = []

    #Remove every file that is in the dir_structure
    for file in all_files:
        if file not in repeated_files:  # Ensure no duplicates
            file_names.append(file)
        else:
            repeated_files.append(file)

    for file in file_names:
        destination = input(f"{file} is going to: {repeated_files}")
        print(f"Moving {file} to {destination}")
        #move_files(DESKTOP_PATH, DIR_NAMES)



def main():
    """Main function to run the script."""
    #create_directories(DESKTOP_PATH, DIR_NAMES)
    select_files(DESKTOP_PATH, DIR_NAMES)
    #move_files(DESKTOP_PATH, DIR_NAMES)

if __name__ == "__main__":
    main()
