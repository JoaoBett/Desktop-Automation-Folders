import os

#DIR_NAMES = {"uni":["sgi", "p1", "redes", "bd"], "misc":["fotos", "jo"], "estudos": ["desenv-Web"]}
DIR_NAMES= "uni"
PATH = "C:\\Users\\joaog\\Desktop"
try:    
    full_path = os.path.join(PATH, DIR_NAMES)

    os.mkdir(path=full_path)
    print("Directory '% s' created "% DIR_NAMES)
except FileExistsError:
    print(f"The file already exists on {PATH}.")
        