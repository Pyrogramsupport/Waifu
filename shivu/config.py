class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7350197183"
    sudo_users = "7350197183"
    GROUP_ID = -1002159833810
    TOKEN = "7328682504:AAEPBlgQ6Tr6Dvv3oOYwba3EywQ4hm2kjTA"
    mongo_url = "mongodb+srv://Hanuman:Siva@bot.7afxmsg.mongodb.net/?retryWrites=true&w=majority&appName=Bot"
    PHOTO_URL = ["https://telegra.ph/file/b89f8d3daed456c1c5ddf.jpg", "https://telegra.ph/file/18eb0aa99929796cf62bb.jpg", "https://telegra.ph/file/fd1c9426df1fe6c8b1ea5.jpg"]
    SUPPORT_CHAT = "animecatchersupport"
    UPDATE_CHAT = "animecatcherupdates"
    BOT_USERNAME = "animecatcher_x_robot"
    CHARA_CHANNEL_ID = "-1002156837160"
    api_id = 19042248
    api_hash = "a1d443cb79941a89c493f22abf4f84cb"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
