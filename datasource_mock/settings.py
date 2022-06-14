import os
PATH_TO_DATA = os.getenv('PATH_TO_DATA')

# In a real project I would use pydantic.BaseSettings,
# but here I just show different ways to read env variables.
# Didn't use dotenv or envparse because of the requirements to this task
