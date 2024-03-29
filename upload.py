import xnat
import os
from qc import SUBID

# 1) Declare constant variables
TAR_SUBFOLDER=f'C:/Users/Khadija_Hammawa/Documents/GitHub/xnat_sftp/BDV01_CMH_000{SUBID}.tar.gz'
PROJ='BDV01_CMH'
DEST='/prearchive'
SUB_LABEL=f'BDV01_CMH_000{SUBID}'

try:
    if not os.path.exists(TAR_SUBFOLDER):
        raise FileNotFoundError
except FileNotFoundError:
    print("Subject tar.gz folder NOT found")

# 2) Connect to server
session = xnat.connect('https://xnat.camh.ca/xnat', user='khadija_hammawa')

# 3) Get the project
project = session.projects[PROJ]

# Initialize list of exisiting subjects
existing_subjects = []

# 4) Get a list of subjects
for subject in project.subjects.values():
    existing_subjects.append(subject.label)

# 4)
if SUB_LABEL not in existing_subjects:
    # Create a new subject
    subject = session.classes.SubjectData(parent=project, label=SUB_LABEL)
else:
    # Skip creating a new subject
    print(f"Subject {SUB_LABEL} already exists.")

# import data to prearchive
prearchive_session = session.services.import_(TAR_SUBFOLDER, project=PROJ, destination=DEST)

# close connection to server
session.disconnect()