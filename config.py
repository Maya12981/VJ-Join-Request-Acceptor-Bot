from os import environ

API_ID = int(environ.get("API_ID", "20284828"))
API_HASH = environ.get("API_HASH", "a980ba25306901d5c9b899414d6a9ab7")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002258864841"))
ADMINS = int(environ.get("ADMINS", "6797820880"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://worep38024:eQkzkfjayr6cVtkI@cluster0.mtradfw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
