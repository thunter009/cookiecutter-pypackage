import os
from .utils import load_env


load_env()

# general settings
# define global variables here, to have environment variables override hard coded defaults
# out of the box, use the pattern:
# VARIABLE = os.getenv("VARIABLE", "default")