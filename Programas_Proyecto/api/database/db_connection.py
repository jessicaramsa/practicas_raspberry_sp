from pymongo import MongoClient
from pprint import pprint

def get_db_url():
    pathFile = '../config/config.json'
    with open(pathFile, encoding='utf-8') as config_file:
        return json.load(config_file) or None

# connect to MongoDB
client = MongoClient(get_db_url())
db  = client.admin

# issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
