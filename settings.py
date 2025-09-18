#this will be the config file for main app.. for calling in all the imp configs

import os

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')



#this takes in the API key from the env variables
# basically, this setting file will be called as the config file for the main app...
# & other imp configs can be added here if needed