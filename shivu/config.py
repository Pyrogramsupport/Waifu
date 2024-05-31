class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7350197183"
    sudo_users = "7350197183"
    GROUP_ID = -1002159833810
    TOKEN = "7328682504:AAEIy7vJ3jfphSVgDE-tA8P7TxQ8NcIX0z8"
    mongo_url = "mongodb+srv://Siva:siva@secure.ffezokv.mongodb.net/?retryWrites=true&w=majority&appName=Secure"
    PHOTO_URL = ["https://telegra.ph/file/b89f8d3daed456c1c5ddf.jpg", "https://telegra.ph/file/18eb0aa99929796cf62bb.jpg"]
    SUPPORT_CHAT = "animecatchersupport"
    UPDATE_CHAT = "naimecatcherupdates"
    BOT_USERNAME = "animecatcher_x_robot"
    CHARA_CHANNEL_ID = "-1002156837160"
    api_id = 19042248
    api_hash = "a1d443cb79941a89c493f22abf4f84cb"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
