import pymongo
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_collection = database['users']

async def present_in_usconfigerbase(user_id : int):
    found = user_collection.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False

async def add_to_userbase(user_id: int):
    user_collection.insert_one({'_id': user_id})
    return

async def get_users():
    user_docs = user_collection.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids
    
async def del_from_userbase(user_id: int):
    user_collection.delete_one({'_id': user_id})
    return

async def get_status():
    filters = filter_collection.find()
    filters_no = 0
    text = 0
    photo = 0
    video = 0
    audio = 0
    document = 0
    animation = 0
    sticker = 0
    voice = 0 
    videonote = 0 
    
    for filter in filters:
        type = filter['type']
        if type == 'Text':
            text += 1 
        elif type == 'Photo':
            photo += 1 
        elif type == 'Video':
            video += 1 
        elif type == 'Audio':
            audio += 1 
        elif type == 'Document':
            document += 1
        elif type == 'Animation':
            animation += 1
        elif type == 'Sticker':
            sticker += 1 
        elif type == 'Voice':
            voice += 1
        elif type == 'Video Note':
            videonote += 1 

        filters_no += 1
    
    user_collection = database['users']
    no_users = user_collection.find().count()
    
    stats_text = f"""<b>Statistics</b>
    
Total users: {no_users}
Total filters: {filters_no}
Text filters: {text}
Photo filters: {photo}
Video filters: {video}
Audio filters: {audio}
Document filters: {document}
Animation filters: {animation}
Sticker filters: {sticker}
Voice filters: {voice}
Video Note filters: {videonote}"""

    return stats_text
