<<<<<<< HEAD

import os
import re
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abel@localhost:5432/fyyur"
SQLALCHEMY_TRACK_MODIFICATIONS=True
=======

import os
import re
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
'''uri = os.getenv("postgres://postgres:abel@localhost:5432/fyyure") 
 # or other relevant config var
if uri.startswith("postgres://postgres:abel@localhost:5432/fyyure"):
  uri = uri.replace("postgres://postgres:abel@localhost:5432/fyyure", "postgresql://postgres:abel@localhost:5432/fyyure", 1)'''

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:abel@localhost:5432/fyyure"
SQLALCHEMY_TRACK_MODIFICATIONS=True
>>>>>>> c5650ae46363813b7f6e8e3a0e6d9b9b03519871
