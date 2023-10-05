# Instead of  Creating Folder Structure Manually , if you are creating this type of Template file , one time effort.
# Next time you don't need to create this file from very scratch , you just need to exceute this and it will create
# Folder Structure automatically for me.


# So I'll try to create this Folder Structure automatically in a Pythonic Way automatically.

import os
from pathlib import Path
import logging



# We will log in each and every thing that we are doing
# So whenever this template.py will be running it will generate some Logging


# So basically we wil try to have one log format that tells - 
# basically insitializing logging level , basically you want to log information label only
# then we are specifying time , that is current ascitime or you can say the current time , with that the logging message you want to put.

logging.basicConfig(level=logging.INFO , format = '[%(asctime)s]: %(message)s:')

# Then we will write our Project_name
project_name = "cnnClassifier"

# List of Files or Folder you want to create
list_of_files = [
    # The first folder we want to create .github , so we need this whenever we are doing the deployment
    # So here we'll be writing CI/CD related comment 
    # So if you comment any empty folder it will reflect in your GitHub, you should have present something in the folder.
    ".github/workflows/.gitkeep",
    # Inside Src folder i'll be creating one folder that is project_name which is cnnClassifier.
    # So it will be some local package , so we need to specifiy __init__.py constructor file inside it.
    # For eg. if we have some file inside it lets say Model.py , so from any app or main app.py we can import this Model.py file
    f"src/{project_name}/__init__.py",
    # After that we'll be creating another Folder Called Components , inside that we'll create another Constructor file
    # bcoz component will be another local paakage folder
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    # Now this configuration.py will contain all the configuration in configuration.py
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    # Folder and File are done, now we need some file here
    "config/config.yaml",
    "dvc.yaml",
    "parms.yaml",
    # So it wil  contain all the Requriements Pacakge of our Project
    "requirements.txt",
    "setup.py",
    # Why are we using this resource Folder , bcoz before performing any or building any actual components, 
    # I'll perform some Notebook Experiments.
    "resource/trials.ipynb",
    "templates/index.html",

# So for now these are the files that I need Unitl now , if i need something else we'll edit here.

]

# Lets now create logic

# Why are we using forward slash here bcoz we know that in Windows Operating System uses Backward Slash instead of Forward Slash.
# So if you are not handling these kinds of Forward Slash Path , it will kind of Throw some Errors , whenever you execute your code.
# So when we are looping it will specify it is a windows path.

# Note - Forward Slash we use in our Linux Operating System.

for filepath  in list_of_files:
    filepath = Path(filepath)
    # Note - One thing to Note above is list_of_files contains the folder names , as well as the file names for eg:-__init__.py
    # FOr that we will use function  os.split    , which will return the filerdirectory or folder name as well as the filename.
    filedir , filename = os.path.split(filepath)


    # Note:- This will create the directory for us
    # If this Filedir or You can say Folder name is not empty
    if filedir !="":
        # WE give another parameter over here  exist_ok = True ,which means if its already created don't create it again
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file :{filename} ")

    # Now after creating the Directory we need to create the file as well.
    # First we will chk if the current file exists or not , & if it doesn't exists 
    # Define another logic
    # Note - Remember os.path.getsize(filepath) if it returns some number that means it contains some of the Text Here
    # You can try it out with any File in any of your Folder , if it returns some Numeric Value that means it conatins
    # Some Text inside it.
    # Remember it can be any file.
    # So if there is any text i don't want to replace that file with my new file , we are just checking.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        # SO if not the case above we'll create the file.
        with open(filepath,"w") as f:
            # We only want to create the FIle , so after creating i'll just pass it.
            pass
        # Then we'll log the Information
        logging.info(f"Creating empty file :{filepath}")


    # After that We'll write or else condition
    # SO if the Size of os.path.getsize is not equal to 0 , then it means there is already existing file.
    else:
        logging.info(f"{filename} is already exists")