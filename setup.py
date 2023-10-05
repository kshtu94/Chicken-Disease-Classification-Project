# So this code inside setup.py will remain common for every setup.py file.

# So first need to import setuptools
import setuptools

# Then open Readme file into the read mode
with open("README.md" ,"r" ,encoding="utf-8") as f:
    # So this long_description is if you want to publish this thing as a pypy package in future you need this thing.
    long_description = f.read()


# You can easily see what is the versio of your classifier
__version__ = "0.0.0"


REPO_NAME = "Chicken-Disease-Classification-Project"
# This is the username of my GitHub
AUTHOR_USER_NAME = "kshtu94"
# Then Source repo name , which is inside src\cnnClassifier
SRC_REPO = "cnnClassifier "
#Then AUthor Email address
AUTHOR_EMAIL = "kshtu94@gmail.com"




setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app",
    long_description = long_description,
    long_description_content = "text/makdown",
    url = "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" = f"https://github.com/"
    }

)

# F-string or You can say f-string provide a way to embed expressions inside string literals, using a minimal syntax.

# Note-  We wont be publishing this thing as a pypy package , so instead of this we will be hosting this thing as a local 
# package ,that' why we are creating setup.py 